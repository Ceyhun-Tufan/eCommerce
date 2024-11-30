from pydantic import BaseModel,Field
from typing import Optional
from datetime import datetime


# serializer


class ProductBase(BaseModel):
    name: str = Field(..., example="Laptop")
    description: Optional[str] = Field(default="", example="A high-performance laptop")
    price: float = Field(..., example=1500.00)
    image_path: str = Field(..., example="/path/to/image.jpg")
    stock:int = Field(...,example=1)

    class Config:
        orm_mode = True


class ProductCreate(ProductBase):
    seller_id:int = Field(...,example=123)

    class Config:
        orm_mode = True 

class ProductUpdate(ProductBase):
    name: Optional[str] = Field(None,example="Laptop")
    description: Optional[str] = Field(None,example="A good laptop")
    price: Optional[float] = Field(None,example=100.00)
    image_path: Optional[str] = Field(None,example="img/xxx.jpg")
    stock: Optional[int] = Field(None,example=100)


    class Config:
        orm_mode = True 

class ProductResponse(ProductBase):
    id: int
    seller_id: int
    name:str
    description: str
    price: float
    created_at: datetime
    updated_at: Optional[datetime]
    stock: int  # Yeni alan

    class Config:
        orm_mode = True