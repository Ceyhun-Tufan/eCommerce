from fastapi import FastAPI,Depends,HTTPException
from database import Base,engine
from pathlib import Path
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from schemas import ProductBase,ProductCreate,ProductUpdate,ProductResponse
import crud
from typing import List


app = FastAPI()
UPLOAD_DIR = Path("uploads/")  # Görsellerin saklanacağı klasör
UPLOAD_DIR.mkdir(exist_ok=True) 

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        # Modelleri veritabanında oluştur
        await conn.run_sync(Base.metadata.create_all)



@app.get("/api/products/",response_model=list[ProductResponse]) # perfect
async def get_all_products(db:AsyncSession= Depends(get_db)):
    all_products = await crud.get_products(db)
    return all_products

@app.post("/api/products/",response_model=ProductCreate) # perfect
async def create_product(product_data: ProductCreate,db:AsyncSession = Depends(get_db)):
    new_product = await crud.create_product(db,product_data)      
    return new_product



@app.get("/api/product/{product_id}",response_model=ProductResponse)
async def get_single_product(product_id:int,db:AsyncSession = Depends(get_db)):
    product = await crud.get_product(db,product_id)
    if product is None:
        raise HTTPException(status_code=400,detail="Could not find that particular product")
    return product

