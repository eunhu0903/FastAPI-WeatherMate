from sqlalchemy import Column, String, Integer, Boolean
from db.database import Base
from typing import Optional

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email= Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active: Optional[bool] = True