from fastapi import APIRouter

orders_router=APIRouter(
    prefix='/orders',
    tags=['order']
)

@order_router.get('/')
async def hello():
    return {"message":"PIZZZA Order"}
