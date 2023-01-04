from fastapi import APIRouter

from dao.productLinesDao import ProductLines
from models.productLines import ProductLinesModel

router = APIRouter(prefix='/productLines', tags=['productLines'])
# /productLines/all
@router.get('/all')
async def getProductLines():
  return {'productLines' : ProductLines.getAllProductLines()}

@router.post('/new', response_model=ProductLinesModel)
async def addProductLines(productLines : ProductLinesModel):
  return productLines