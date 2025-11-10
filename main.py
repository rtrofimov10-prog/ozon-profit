# -*- coding: utf-8 -*-
import os
import httpx
from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from typing import List, Dict, Any
from pathlib import Path

app = FastAPI(
    title="OzonProfit",
    description="Full-featured web application for analytics, accounting and management of stores on Ozon",
    version="2.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration from environment
OZON_API_URL = "https://api-seller.ozon.ru"
OZON_SELLER_API_KEY = os.getenv("OZON_SELLER_API_KEY", "")
OZON_CLIENT_ID = os.getenv("OZON_CLIENT_ID", "")

class ProductData(BaseModel):
    product_id: int
    title: str
    price: float
    quantity: int

class OrderData(BaseModel):
    order_id: int
    status: str
    total_price: float

class OzonClient:
    def __init__(self, api_key: str, client_id: str):
        self.api_key = api_key
        self.client_id = client_id
        self.base_url = OZON_API_URL
    
    async def get_products(self):
        """Get list of products from Ozon API using stocks endpoint"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.base_url}/v1/product/info/stocks",
                    headers={
                        "Client-Id": self.client_id,
                        "Api-Key": self.api_key,
                        "Content-Type": "application/json"
                    },
                    json={"page": 1, "page_size": 100},
                    timeout=10
                )
                
                if response.status_code == 200:
                    data = response.json()
                    print(f"Ozon API Products Response: {data}")
                    items = data.get("items", [])
                    return items if items else []
                else:
                    print(f"Ozon API Error (Products): {response.status_code} - {response.text}")
                    return []
        except Exception as e:
            print(f"Error getting products: {e}")
            return []
    
    async def get_orders(self):
        """Get list of orders from Ozon API (FBS)"""
        try:
            async with httpx.AsyncClient() as client:
                # Set date range for last 30 days
                now = datetime.utcnow()
                start_date = (now - timedelta(days=30)).isoformat() + "Z"
                end_date = now.isoformat() + "Z"
                
                response = await client.post(
                    f"{self.base_url}/v3/posting/fbs/list",
                    headers={
                        "Client-Id": self.client_id,
                        "Api-Key": self.api_key,
                        "Content-Type": "application/json"
                    },
                    json={
                        "limit": 100,
                        "offset": 0,
                        "filter": {
                            "processed_at_from": start_date,
                            "processed_at_to": end_date,
                            "status": ""
                        }
                    },
                    timeout=10
                )
                
                if response.status_code == 200:
                    data = response.json()
                    print(f"Ozon API Orders Response: {data}")
                    postings = data.get("postings", [])
                    return postings if postings else []
                else:
                    print(f"Ozon API Error (Orders): {response.status_code} - {response.text}")
                    return []
        except Exception as e:
            print(f"Error getting orders: {e}")
            return []

ozon_client = OzonClient(OZON_SELLER_API_KEY, OZON_CLIENT_ID)

@app.get("/")
async def read_root():
    """Serve the main HTML file"""
    html_file = Path(__file__).parent / "public" / "index.html"
    if html_file.exists():
        return FileResponse(html_file)
    return {"error": "HTML file not found"}

@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "ok"}

@app.get("/api/v1/dashboard")
async def get_dashboard():
    """Get dashboard data"""
    try:
        products = await ozon_client.get_products()
        orders = await ozon_client.get_orders()
        
        total_products = len(products) if isinstance(products, list) else 0
        total_orders = len(orders) if isinstance(orders, list) else 0
        
        return {
            "status": "success",
            "data": {
                "total_products": total_products,
                "total_orders": total_orders,
                "products": products[:5] if isinstance(products, list) else [],
                "recent_orders": orders[:5] if isinstance(orders, list) else []
            }
        }
    except Exception as e:
        print(f"Error in dashboard: {e}")
        return {
            "status": "error",
            "message": str(e),
            "data": {"total_products": 0, "total_orders": 0, "products": [], "recent_orders": []}
        }

@app.get("/api/v1/products")
async def get_products():
    """Get products list"""
    try:
        products = await ozon_client.get_products()
        return {"status": "success", "data": products if isinstance(products, list) else []}
    except Exception as e:
        return {"status": "error", "message": str(e), "data": []}

@app.get("/api/v1/orders")
async def get_orders():
    """Get orders list"""
    try:
        orders = await ozon_client.get_orders()
        return {"status": "success", "data": orders if isinstance(orders, list) else []}
    except Exception as e:
        return {"status": "error", "message": str(e), "data": []}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
