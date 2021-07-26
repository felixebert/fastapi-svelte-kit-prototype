from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import products, orders, token, users

app = FastAPI()

origins = [
    # TODO add configuration value
    "http://localhost:3000",
]

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
