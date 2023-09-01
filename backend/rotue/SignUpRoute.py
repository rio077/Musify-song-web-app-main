from fastapi import APIRouter
from schema.SignUpSchema import  post_SignUpSchema,get_SignUpData,get_oneSignUp, delete_SignUp
from model.SignUp import SignUpModel  # Assuming "model" is at the same level as the current module.

SignUp = APIRouter()

@SignUp.post("/SignUp/Create/", tags=['SignUp'], summary="Create details")
def read_root(data: SignUpModel):  # Use the absolute import path for SignUpModel.
    """
    ### Add a job [Documentation Here](https://docs.google.com/document/d/11b0gBImZmHH_FCxeZxtvVJ7UF7VAcB3EF_KKSIIjEmo/edit#heading=h.4fpya9hkk4bs) 
    """
    response = post_SignUpSchema(data)
    return {"response": response}

@SignUp.get("/SignUp/getDetails/", tags=['SignUp'], summary="get info")
def read_root():  # Use the absolute import path for SignUpModel.
    """
    ### Add a job [Documentation Here](https://docs.google.com/document/d/11b0gBImZmHH_FCxeZxtvVJ7UF7VAcB3EF_KKSIIjEmo/edit#heading=h.4fpya9hkk4bs) 
    """
    response = get_SignUpData()
    return {"response": response}

@SignUp.get("/SignUp/getDetails_one/", tags=['SignUp'], summary="Get Info Of One")
def read_root(SignUpId):  # Use the absolute import path for SignUpModel.
    """
    ### Add a job [Documentation Here](https://docs.google.com/document/d/11b0gBImZmHH_FCxeZxtvVJ7UF7VAcB3EF_KKSIIjEmo/edit#heading=h.4fpya9hkk4bs) 
    """
    response = get_oneSignUp(SignUpId)
    return {"response": response}


@SignUp.delete("/SignUp/deleteSignUp/", tags=['SignUp'], summary="Create Jobs")
def read_root(SignUpId):  # Use the absolute import path for SignUpModel.
    """
    ### Add a job [Documentation Here](https://docs.google.com/document/d/11b0gBImZmHH_FCxeZxtvVJ7UF7VAcB3EF_KKSIIjEmo/edit#heading=h.4fpya9hkk4bs) 
    """
    response = delete_SignUp(SignUpId)
    return {"response": response}