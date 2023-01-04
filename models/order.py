from pydantic import BaseModel
from datetime import date


class OrderModel(BaseModel):
  orderNumber : str
  orderDate : date
  requiredDate : date
  shippedDate : date
  status : str
  comments : str
  customerNumber : str