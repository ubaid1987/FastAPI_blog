from pydantic import BaseModel

# Schema for API body paramter
class Blog(BaseModel):
    title: str
    body: str
    author: str