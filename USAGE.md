# OzonProfit - Руководство пользователя

## Содержание

1. [Введение](#введение)
2. [Быстрый старт](#быстрый-старт)
3. [API Endpoints](#api-endpoints)
4. [Примеры использования](#примеры-использования)
5. [Функции приложения](#функции-приложения)
6. [Решение проблем](#решение-проблем)

## Введение

OzonProfit - это веб-приложение для аналитики, учета и управления магазином на Ozon. Приложение предоставляет полный набор инструментов для:

- Отслеживания продаж и доходов
- Анализа данных о товарах
- Управления финансами
- Администрирования товаров и компаний

**Приложение развернуто и доступно по адресу:** https://ozon-profit.onrender.com/

## Быстрый старт

### Шаг 1: Открыть приложение

Переходите по ссылке: https://ozon-profit.onrender.com/

Вы увидите приветственное сообщение API.

### Шаг 2: Проверить статус приложения

Зайдите на endpoint проверки здоровья:
https://ozon-profit.onrender.com/health

Должно вернуться: `{"status":"ok"}`

### Шаг 3: Просмотреть документацию API

Доступна интерактивная документация:
- Swagger UI: https://ozon-profit.onrender.com/docs
- ReDoc: https://ozon-profit.onrender.com/redoc

## API Endpoints

### 1. Главная страница API

**URL:** `GET /`

**Описание:** Возвращает информацию о приложении

**Response:**
```json
{
  "message": "Welcome to OzonProfit API",
  "version": "1.0.0",
  "docs": "/docs",
  "redoc": "/redoc"
}
```

### 2. Проверка здоровья приложения

**URL:** `GET /health`

**Описание:** Проверяет, работает ли приложение

**Response:**
```json
{
  "status": "ok"
}
```

### 3. Получить данные дашборда

**URL:** `GET /api/v1/dashboard`

**Описание:** Возвращает данные дашборда с статистикой

**Response:**
```json
{
  "title": "Dashboard",
  "stats": {
    "total_sales": 0,
    "total_revenue": 0,
    "active_products": 0
  }
}
```

## Примеры использования

### Используя браузер

1. Перейдите на https://ozon-profit.onrender.com/
2. В адресной строке добавьте нужный endpoint, например:
   - https://ozon-profit.onrender.com/health
   - https://ozon-profit.onrender.com/api/v1/dashboard

### Используя curl

```bash
# Получить информацию о приложении
curl https://ozon-profit.onrender.com/

# Проверить статус
curl https://ozon-profit.onrender.com/health

# Получить данные дашборда
curl https://ozon-profit.onrender.com/api/v1/dashboard
```

### Используя Python

```python
import requests

# Базовый URL
BASE_URL = "https://ozon-profit.onrender.com"

# Проверить здоровье приложения
response = requests.get(f"{BASE_URL}/health")
print(response.json())

# Получить данные дашборда
response = requests.get(f"{BASE_URL}/api/v1/dashboard")
print(response.json())
```

### Используя JavaScript/Node.js

```javascript
const BASE_URL = "https://ozon-profit.onrender.com";

// Проверить здоровье приложения
fetch(`${BASE_URL}/health`)
  .then(response => response.json())
  .then(data => console.log(data));

// Получить данные дашборда
fetch(`${BASE_URL}/api/v1/dashboard`)
  .then(response => response.json())
  .then(data => console.log(data));
```

## Функции приложения

Планируемые функции для будущих версий:

- ✅ API endpoints для доступа к данным
- ⏳ Интеграция с Ozon Seller API
- ⏳ Dashboard для визуализации данных
- ⏳ Аналитика продаж
- ⏳ Управление товарами
- ⏳ Отчеты по финансам
- ⏳ Управление магазинами и компаниями
- ⏳ React Frontend

## Решение проблем

### Приложение не отвечает

Проверьте:
1. Интернет соединение
2. URL приложения: https://ozon-profit.onrender.com/
3. Попробуйте endpoint здоровья: https://ozon-profit.onrender.com/health

### Ошибка 502 Bad Gateway

Это может означать:
1. Приложение перезагружается (подождите 30 секунд)
2. Сервер на бесплатном плане может "спать" при неактивности (попробуйте еще раз)

### Ошибка CORS

Если получаете ошибку CORS при запросе с браузера, убедитесь, что запрос идет с правильного домена.

## Поддержка

Если у вас есть вопросы или проблемы:

1. Проверьте документацию: https://ozon-profit.onrender.com/docs
2. Просмотрите логи приложения
3. Откройте issue на GitHub

---

**Версия приложения:** 1.0.0  
**Последнее обновление:** November 11, 2025  
**Статус:** Production
