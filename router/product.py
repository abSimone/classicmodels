from fastapi import APIRouter

from dao.productDao import Product
from models.product import ProductModel

router = APIRouter(prefix='/products', tags=['products'])
# /products/all
@router.get('/all')
async def getProduct():
  return {'products' : Product.getAllProduct()}

@router.post('/new', response_model=ProductModel)
async def addProduct(product : ProductModel):
  return product