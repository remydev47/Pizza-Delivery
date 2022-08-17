from fastapi import APIRouter

auth_router=APIRouter()

@auth_router.get('/')
async def hello():
    return {"message":"Hello world"}
