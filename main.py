# -*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="OzonProfit",
    description="Full-featured web application for analytics, accounting and management of stores on Ozon",
    version="1.0.0"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    """Main API endpoint"""
    return {
        "message": "Welcome to OzonProfit API",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "ok"}

@app.get("/api/v1/dashboard")
def get_dashboard():
    """Get dashboard data"""
    return {
        "title": "Dashboard",
        "stats": {
            "total_sales": 0,
            "total_revenue": 0,
            "active_products": 0
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
