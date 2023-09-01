from fastapi import APIRouter
from schema.SongsSchema import  post_SongsSchema,get_SongsData,delete_Songs
from model.Songs import SongsModel  # Assuming "model" is at the same level as the current module.

Songs = APIRouter()

@Songs.post("/Songs/Create/", tags=['Songs'], summary="Create details")
def read_root(data: SongsModel):  # Use the absolute import path for SongsModel.
    """
    ### Add a job [Documentation Here](https://docs.google.com/document/d/11b0gBImZmHH_FCxeZxtvVJ7UF7VAcB3EF_KKSIIjEmo/edit#heading=h.4fpya9hkk4bs) 
    """
    response = post_SongsSchema(data)
    return {"response": response}

@Songs.get("/Songs/getDetails/", tags=['Songs'], summary="get info")
def read_root():  # Use the absolute import path for SongsModel.
    """
    ### Add a job [Documentation Here](https://docs.google.com/document/d/11b0gBImZmHH_FCxeZxtvVJ7UF7VAcB3EF_KKSIIjEmo/edit#heading=h.4fpya9hkk4bs) 
    """
    response = get_SongsData()
    return {"response": response}

@Songs.delete("/Songs/deleteSongs/", tags=['Songs'], summary="Create Jobs")
def read_root(SongsId):  # Use the absolute import path for SongsModel.
    """
    ### Add a job [Documentation Here](https://docs.google.com/document/d/11b0gBImZmHH_FCxeZxtvVJ7UF7VAcB3EF_KKSIIjEmo/edit#heading=h.4fpya9hkk4bs) 
    """
    response = delete_Songs(SongsId)
    return {"response": response}