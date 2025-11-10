# -*- coding: utf-8 -*-
import os
import httpx
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
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.base_url}/v2/product/list",
                    headers={
                        "Client-Id": self.client_id,
                        "Api-Key": self.api_key,
                        "Content-Type": "application/json"
                    },
                    json={"limit": 50, "offset": 0},
                    timeout=10
                )
                if response.status_code == 200:
                    return response.json().get("products", [])
                return []
        except Exception as e:
            print(f"Error getting products: {e}")
            return []
    
    async def get_orders(self):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.base_url}/v3/posting/fbs/list",
                    headers={
                        "Client-Id": self.client_id,
                        "Api-Key": self.api_key,
                        "Content-Type": "application/json"
                    },
                    json={"limit": 50, "offset": 0},
                    timeout=10
                )
                if response.status_code == 200:
                    return response.json().get("orders", [])
                return []
        except Exception as e:
            print(f"Error getting orders: {e}")
            return []

ozon_client = OzonClient(OZON_SELLER_API_KEY, OZON_CLIENT_ID)

# Routes
@app.get("/")
async def serve_frontend():
    html_path = Path(__file__).parent / "public" / "index.html"
    if html_path.exists():
        return FileResponse(html_path, media_type="text/html")
    return {"message": "Welcome to OzonProfit API", "version": "2.0.0", "status": "Backend running"}

@app.get("/api/v1/dashboard")
async def get_dashboard():
    try:
        products = await ozon_client.get_products()
        orders = await ozon_client.get_orders()
        return {
            "status": "success",
            "data": {
                "total_products": len(products),
                "total_orders": len(orders),
                "products": products[:5] if products else [],
                "recent_orders": orders[:5] if orders else []
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/products")
async def get_products():
    try:
        products = await ozon_client.get_products()
        return {"status": "success", "data": products}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/orders")
async def get_orders():
    try:
        orders = await ozon_client.get_orders()
        return {"status": "success", "data": orders}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
