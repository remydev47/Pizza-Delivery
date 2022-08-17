from fastapi import FastAPI
from auth_routes import auth_router
from orders_routes import orders_router

app=FastAPI()

app.include_router(auth_router)
app.include_router(orders_router)
