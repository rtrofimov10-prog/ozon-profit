from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="OzonProfit",
    description="Полнофункциональное веб-приложение для аналитики, учета и управления магазином на Ozon",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    """Главная страница API"""
    return {
        "message": "Добро пожаловать в OzonProfit API",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
def health_check():
    """Проверка здоровья приложения"""
    return {"status": "ok"}

@app.get("/api/v1/dashboard")
def get_dashboard():
    """API для получения данных дашборда"""
    return {
        "title": "Дашборд",
        "stats": {
            "total_sales": 0,
            "total_revenue": 0,
            "active_products": 0
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
