from fastapi import APIRouter #permite dividir nuestros router
from schema.user_schema import UserSchema

user_router = APIRouter()

@user_router.get("/")
def user():
    return {"saludo":"hola desde fastapi"}

@user_router.post("/api/user")
def create_user(datauser:UserSchema):
    print(datauser)
