# 🊀 OzonProfit

Полноценное веб-приложение для аналитики, аккаунтинга и управления магазином на Ozon для одного пользователя.

## Технологии

### Backend
- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **API Integration**: Ozon Seller API

### Frontend
- **Library**: React 18+
- **Language**: TypeScript
- **Styling**: TailwindCSS
- **Build Tool**: Vite
- **Charts**: Chart.js + react-chartjs-2

### Deployment
- **Local**: Docker Compose (optional)
- **Database**: PostgreSQL 14+
- **Python**: 3.11+
- **Node.js**: 18+ LTS

## Функциональность

✅ **Дашборд** - Основные метрики и графики  
✅ **Аналитика** - Наблюдение трендов и динамики  
✅ **Финансы** - Подробные транзакции  
✅ **Товары** - Остатки и цены  
✅ **Мои магазины** - Управление магазином  
✅ **Мои компании** - Профиль и реквизиты  

## БЫСТРЫЙ СТАРТ

### 1. Предварительные требования

```bash
Python 3.11+
PostgreSQL 14+
Node.js 18+ LTS
Git
```

### 2. Клонирование репозитория

```bash
git clone https://github.com/rtrofimov10-prog/ozon-profit.git
cd ozon-profit
```

### 3. Настройка Backend

```bash
cd backend

# Создать .env файл
cat > .env << EOF
DATABASE_URL=postgresql://user:password@localhost/ozon_profit
OZON_CLIENT_ID=ваш_client_id
OZON_API_KEY=ваш_api_key
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=True
EOF

# Установить зависимости
pip install -r requirements.txt

# Построить БД
alembic upgrade head

# Запустить server
python -m app.main
```

### 4. Настройка Frontend

```bash
cd frontend

# Установить зависимости
npm install

# Запустить дев сервер
npm run dev
```

Опен http://localhost:5173

## Настройка Ozon API

1. Перейдите на https://seller.ozon.ru
2. Откройте раздел Developer / API
3. Генерируйте Client ID и API Key
4. Сохраните в .env файл backend/

## License

MIT - см. LICENSE для деталей.
