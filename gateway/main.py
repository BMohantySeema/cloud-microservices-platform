from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Gateway is running"}

@app.get("/users")
async def get_users():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://user_service:8001/")
        return response.json()

@app.get("/products")
async def get_products():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://product_service:8002/")
        return response.json()
