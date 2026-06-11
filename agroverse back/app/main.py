from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from contextlib import asynccontextmanager
import os
import uvicorn

from app.database import engine, Base, AsyncSessionLocal
from app.config import settings
from app.routers import auth, products, orders, payment, bonus, admin, ai

ADMIN_PHONE = "админ123"
ADMIN_PASSWORD = "127845"


async def seed_admin():
    """Создаёт админа если его нет"""
    from sqlalchemy import select
    from app.models import User, UserRole, UserTariff
    from app.auth import get_password_hash
    
    async with AsyncSessionLocal() as db:
        res = await db.execute(select(User).where(User.phone == ADMIN_PHONE))
        if res.scalar_one_or_none():
            return
        
        admin = User(
            name="Администратор",
            phone=ADMIN_PHONE,
            email="admin@agroverse.uz",
            password_hash=get_password_hash(ADMIN_PASSWORD),
            role=UserRole.ADMIN,
            tariff=UserTariff.PREMIUM,
            bonus_points=0,
            is_active=True,
        )
        db.add(admin)
        await db.commit()
        print(f"👑 Админ: {ADMIN_PHONE} / {ADMIN_PASSWORD}")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Инициализация при старте и очистка при завершении"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        from sqlalchemy import text
        await conn.execute(text("ALTER TABLE users ADD COLUMN IF NOT EXISTS block_reason TEXT"))
    
    await seed_admin()
    print("🌾 AgroVerse API запущен на Railway")
    print("✅ CORS разрешён для всех источников")
    
    yield
    await engine.dispose()


# ──── FastAPI приложение ────
app = FastAPI(
    title="AgroVerse API",
    version="2.0",
    lifespan=lifespan,
    docs_url="/docs",
    openapi_url="/openapi.json"
)


# ──── Обработчик ошибок валидации ────
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for e in exc.errors():
        errors.append({
            "loc": [str(x) for x in e.get("loc", [])],
            "msg": str(e.get("msg", "Validation error")),
            "type": str(e.get("type", "")),
        })
    return JSONResponse(
        status_code=422,
        headers={"Access-Control-Allow-Origin": "*"},
        content={"detail": errors}
    )


# ──── CORS Middleware ────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
    max_age=600,
)


# ──── Доп. CORS хедеры для ошибок ────
@app.middleware("http")
async def add_cors_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response


# ──── Статические файлы ────
os.makedirs(settings.upload_dir, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=settings.upload_dir), name="uploads")


# ──── Роутеры ────
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(products.router, prefix="/api/products", tags=["products"])
app.include_router(orders.router, prefix="/api/orders", tags=["orders"])
app.include_router(payment.router, prefix="/api/payment", tags=["payment"])
app.include_router(bonus.router, prefix="/api/bonus", tags=["bonus"])
app.include_router(admin.router, prefix="/api/admin", tags=["admin"])
app.include_router(ai.router, prefix="/api/ai", tags=["ai"])


# ──── Базовые endpoints ────
@app.get("/")
async def root():
    return {
        "message": "🌾 AgroVerse API",
        "version": "2.0",
        "status": "running",
        "docs": "/docs"
    }


@app.get("/health")
async def health():
    return {"status": "healthy", "service": "agroverse-api"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)