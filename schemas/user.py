from pydantic import BaseModel

class UserSchemaOut(BaseModel):
    id: int
    username: str



class UserSchemaIn(BaseModel):
    username: str
