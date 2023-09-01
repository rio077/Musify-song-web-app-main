from pydantic import BaseModel

class SongsModel(BaseModel):
    id:int
    title:str
    audioUrl:str
   