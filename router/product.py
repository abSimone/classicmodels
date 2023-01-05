from fastapi import APIRouter, status
from typing import List
from dao.productDao import Product
from models.product import ProductModel

router = APIRouter(prefix='/products', tags=['products'])
# /products/all
@router.get('/all',response_model=List[ProductModel], response_model_exclude={'productScale', 'productVendor', 'productDescription'})
async def getProduct():
  return Product.getAllProduct()

@router.post('/new', response_model=ProductModel, response_model_include={'productCode'}, status_code=status.HTTP_201_CREATED)
async def addProduct(product : ProductModel):
  return product