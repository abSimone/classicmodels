from fastapi import APIRouter, status
from typing import List
from dao.ordersDao import Orders
from models.order import OrderModel

router = APIRouter(prefix='/orders', tags=['orders'])


@router.get(
    '/all',
    response_model=List[OrderModel],
    response_model_exclude_none=True,
    response_model_include={'orderNumber', 'orderDate', 'status', 'customerNumber'})
async def getOffices():
    return Orders.getAllOrders()


@router.post('/new', response_model=OrderModel, response_model_include={'orderNumber'}, status_code=status.HTTP_201_CREATED)
async def addOrder(order: OrderModel):
    return order
