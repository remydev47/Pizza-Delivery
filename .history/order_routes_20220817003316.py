from fastapi import APIRouter

order_router=APIRouter()

@order_router.get('/')
async def hello():
    return {"message":"Hello world"}
