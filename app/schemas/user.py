from pydantic import BaseModel

class UserCreate(BaseModel):
    username:str
    

class UserResponse(BaseModel):
    id:int
    username:str
    class config:
        orm_mode=True