from pydantic import BaseModel


class BaseURL(BaseModel):
    target_url: str


class URL(BaseURL):
    clicks: int

    class Config:
        orm_mode = True
