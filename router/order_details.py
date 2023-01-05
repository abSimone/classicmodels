from fastapi import APIRouter

from dao.orderDetailDao import orderDetails

from models.order_details import Order_details_model

from typing import List

router = APIRouter(prefix='/order_details', tags=['order_details'])

@router.get(
    '/all',
    response_model = List[Order_details_model],
    response_model_exclude_none = True,
    response_model_exclude = {'orderLineNumber'})
async def getOrderDetails():
    return orderDetails.getAllOrdersDetails()

@router.post('/new', response_model = Order_details_model)
async def addOrderDetail(order_detail : Order_details_model):
    return order_detail