# 🌾 AgroVerse — Локальный запуск

## Требования
- [Docker Desktop](https://www.docker.com/products/docker-desktop) (включает Docker + Docker Compose)

## Быстрый старт

### Windows
Двойной клик на `ЗАПУСК.bat`

### Linux / Mac
```bash
chmod +x ЗАПУСК_LINUX.sh
./ЗАПУСК_LINUX.sh
```

## Ручной запуск

### 1. Запуск бэкенда
```bash
cd "agroverse back"
docker compose up -d --build
```

### 2. Открыть фронтенд
Открой файл `agroverse front/index.html` в браузере.

## Адреса
| Сервис | URL |
|--------|-----|
| Фронтенд | `agroverse front/index.html` |
| Бэкенд API | http://localhost:8000 |
| Swagger Docs | http://localhost:8000/docs |
| PostgreSQL | localhost:5432 |

## Дефолтный admin
- **Телефон:** `+998000000000`
- **Пароль:** `admin123`

## Остановка
```bash
cd "agroverse back"
docker compose down
```

## Структура
```
agroverse-ready/
├── agroverse back/          # FastAPI + PostgreSQL
│   ├── main.py              # Основной файл бэкенда
│   ├── Dockerfile           # Docker образ
│   ├── docker-compose.yml   # Запуск postgres + app
│   ├── requirements.txt     # Python зависимости
│   └── app/                 # Роутеры, модели, схемы
├── agroverse front/         # Vanilla HTML/CSS/JS
│   ├── index.html
│   ├── css/style.css
│   ├── js/
│   └── assets/
├── ЗАПУСК.bat               # Windows запуск
└── ЗАПУСК_LINUX.sh          # Linux/Mac запуск
```
