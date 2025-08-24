from fastapi import APIRouter

router = APIRouter(prefix="/users")

fake_users = []

@router.post("/")
def create_user(name: str, email: str):
    user = {"id": len(fake_users)+1, "name": name, "email": email}
    fake_users.append(user)
    return user

@router.get("/")
def list_users():
    return fake_users
