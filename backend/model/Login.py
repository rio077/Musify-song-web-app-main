from pydantic import BaseModel

class LoginModel(BaseModel):
   UserName:str
   UserPassword:str