from pydantic import BaseModel, Field

class PostCreate(BaseModel):
    text: str = Field(max_length=1024)

class PostDelete(BaseModel):
    postID: int