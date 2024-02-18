from pydantic import BaseModel



class PostSchemaOut(BaseModel):
    id: int
    title: str
    content: str
    category: str


class PostSchemaIn(BaseModel):
    title: str
    content: str
    author_id: int
    category: str
