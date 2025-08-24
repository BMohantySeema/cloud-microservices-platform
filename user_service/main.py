from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "User Service is running"}

@app.get("/users")
def list_users():
    return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
