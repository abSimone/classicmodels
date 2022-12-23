from dao.EmployeeDao import EmployeeDao
from dto.office import Office
from dao.customersDao import CustomersDao
from dao.ordersDao import Orders

# employeeNumber1 =int(input("Inserisci un codice dell'employee : "))
# result=EmployeeDao.getOfficeByEmployeeNumber(employeeNumber1)

# for e in result:
#     print(e)
# order = Orders.getOrdersByProductCode('S10_1678')

customer = CustomersDao.getAllCustomers()

for e in customer:
    print(e)





        
    