from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Product Service is running"}

@app.get("/products")
def list_products():
    return [{"id": 1, "name": "Laptop"}, {"id": 2, "name": "Phone"}]
