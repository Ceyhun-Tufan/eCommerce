from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from models import Product
from schemas import ProductCreate, ProductUpdate


# Ürün oluşturma
async def create_product(db: AsyncSession, product: ProductCreate) -> Product:
    new_product = Product(**product.model_dump())  # Product'ı oluştur
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product


# Tüm ürünleri listeleme
async def get_products(db: AsyncSession):
    result = await db.execute(select(Product))
    return result.scalars().all()


# Tek bir ürünü ID ile getirme
async def get_product(db: AsyncSession, product_id: int):
    try:
        result = await db.execute(select(Product).where(Product.id == product_id))
        return result.scalar_one()
    except NoResultFound:
        return None


# Ürün güncelleme
async def update_product(db: AsyncSession, product_id: int, product_data: ProductUpdate):
    product = await get_product(db, product_id)
    if not product:
        return None
    for key, value in product_data.model_dump(exclude_unset=True).items():
        setattr(product, key, value)
    await db.commit()
    await db.refresh(product)
    return product


# Ürün silme
async def delete_product(db: AsyncSession, product_id: int):
    product = await get_product(db, product_id)
    if not product:
        return None
    await db.delete(product)
    await db.commit()
    return product
