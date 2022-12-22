# File che utilizzeremo in futuro :D
from dao.ordersDao import Orders
from dto.ordersDto import Ordersdto

result=Orders.getAllOrders()
for r in result:
    print(r)