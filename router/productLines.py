from fastapi import APIRouter
from typing import List
from dao.productLinesDao import ProductLines
from models.productLines import ProductLinesModel

router = APIRouter(prefix='/productLines', tags=['productLines'])
# /productLines/all
@router.get('/all',response_model=List[ProductLinesModel], response_model_include={'productLine', 'textDescription'})
async def getProductLines():
  return  ProductLines.getAllProductLines()

@router.post('/new', response_model=ProductLinesModel, response_model_include={'productLine', 'textDescription'})
async def addProductLines(productLines : ProductLinesModel):
  return productLines