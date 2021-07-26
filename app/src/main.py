from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import products, orders, token, users
from .lib.config import Settings

settings = Settings()
app = FastAPI()

if settings.CORS_ALLOW_ORIGIN is not None:
    origins = [settings.CORS_ALLOW_ORIGIN]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_methods=["GET", "POST"],
        allow_headers=["*"],
    )

app.include_router(products.router)
app.include_router(orders.router)
app.include_router(token.router)
app.include_router(users.router)
