from pydantic import BaseModel
from typing import Optional # para que el Id se genere sin que el usuario lo ingrese

# el id se va auto generar
class UserSchema(BaseModel):
    id:Optional[str]
    name:  str
    username:str
    pasword:str