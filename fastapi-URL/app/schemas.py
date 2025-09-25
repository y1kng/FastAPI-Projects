from pydantic import BaseModel, HttpUrl
from datetime import datetime

class UserCheck(BaseModel):  # Request model for checking a user-provided URL
    ori_url: HttpUrl

class SysCheck(BaseModel):  # Response model for system data
    id: int 
    short_one: str
    created_time: datetime
    count_c: int
    class Config:    
        orm_mode = True  # Enable compatibility with SQLAlchemy ORM objects
