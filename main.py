import json
from dao.ordersDao import Orders
from fastapi import FastAPI


result= Orders.getAllOrders()
result_json=json.dumps(result, default=str)
result_tuple=tuple(result)

app = FastAPI()


@app.get("/orders")
def read_root():
    return {result_tuple}