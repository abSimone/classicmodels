from fastapi import APIRouter

from dao.orderDetailDao import orderDetails

from models.order_details import Order_details_model

router = APIRouter(prefix='/order_details', tags=['order_details'])

@router.get('/all')
async def getOrderDetails():
    return {'oDetails' : orderDetails.getAllOrdersDetails()}

@router.post('/new', response_model = Order_details_model)
async def addOrderDetail(order_detail : Order_details_model):
    return order_detail