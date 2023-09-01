from pydantic import BaseModel

class SignUpModel(BaseModel):
   Username:str
   Email:str
   Password:str
   