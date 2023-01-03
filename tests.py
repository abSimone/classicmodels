from dao.ordersDao import Orders
import json

order=Orders.getAllOrders()
lista=[]
for o in order:
    lista.append(o)
rngData = json.dumps(lista,indent=2, default = str)
print(rngData)