from sqlalchemy import Column, Integer, String, DateTime   
from .database import Base
from datetime import datetime


class ShortUrl(Base):
    __tablename__ = "short_urls"

    id = Column(Integer, primary_key=True, index=True)
    ori_url = Column(String, nullable=False, index=True)
    short_one = Column(String, unique=True, index=True, nullable=False)
    created_time = Column(DateTime, default=datetime.utcnow)  # timestamp of creation
    count_c = Column(Integer, default=0)    # access count