from dao.customersDao import CustomersDao
from dao.EmployeeDao import EmployeeDao
from dto.Office import Office

# result = CustomersDao.getAllCustomers()
# print(result)

# risultato_nomi = []
# for customer in result:
#     if len(customer.customerName) <= 6:
#         risultato_nomi.append([customer.contactFirstName, customer.contactLastName])


office = EmployeeDao.getOfficeByEmployeeNumber(1002)

print(office)

print(f"Codice ufficio: {office.officeCode}")
