from fastapi import APIRouter
from schema.LoginSchema import  post_LoginSchema, delete_Login
from model.Login import LoginModel  # Assuming "model" is at the same level as the current module.

Login = APIRouter()

@Login.post("/Login/Create/", tags=['Login'], summary="Create details")
def read_root(data: LoginModel):  # Use the absolute import path for LoginModel.
    """
    ### Add a job [Documentation Here](https://docs.google.com/document/d/11b0gBImZmHH_FCxeZxtvVJ7UF7VAcB3EF_KKSIIjEmo/edit#heading=h.4fpya9hkk4bs) 
    """
    response = post_LoginSchema(data)
    return {"response": response}


@Login.delete("/Login/deleteLogin/", tags=['Login'], summary="Create Jobs")
def read_root(LoginId):  # Use the absolute import path for LoginModel.
    """
    ### Add a job [Documentation Here](https://docs.google.com/document/d/11b0gBImZmHH_FCxeZxtvVJ7UF7VAcB3EF_KKSIIjEmo/edit#heading=h.4fpya9hkk4bs) 
    """
    response = delete_Login(LoginId)
    return {"response": response}
