from fastapi import APIRouter

router = APIRouter(prefix="/products")

fake_products = []

@router.post("/")
def create_product(name: str, price: float):
    product = {"id": len(fake_products)+1, "name": name, "price": price}
    fake_products.append(product)
    return product

@router.get("/")
def list_products():
    return fake_products
