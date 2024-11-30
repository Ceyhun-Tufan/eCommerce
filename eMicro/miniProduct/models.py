from sqlalchemy import Column, Integer, String, Boolean, DateTime,Float
from sqlalchemy.sql import func
from database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    seller_id = Column(Integer)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False, default="")
    price = Column(Float, nullable=False)
    stock = Column(Integer,nullable=False,default=0)
    image_path = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
