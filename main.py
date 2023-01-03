
from dao.productLinesDao import ProductLines
from dao.ordersDao import Orders
from fastapi import FastAPI
from pydantic import BaseModel
import json

class Order(BaseModel):
    orderNumber : str
    orderDate : str
    requiredDate : str
    shippedDate : str | None=None
    status : str
    comments : str | None=None
    customerNumber : str

app=FastAPI()

@app.get('/')
def read_root():
    return {'Hello' : 'World'}

@app.get('/orders')
def read_orders():
    order=Orders.getAllOrders()
    lista=[]
    for o in order:
        o=o.__dict__
        lista.append(o)
    return json.dumps(lista,indent=2,  default=str)

@app.post('/orders/')
async def addOrder(order:Order):
    return order

