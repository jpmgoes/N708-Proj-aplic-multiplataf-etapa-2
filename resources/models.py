from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    availability = Column(Boolean, default=True)
