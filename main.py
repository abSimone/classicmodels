from dao.customersDao import CustomersDao
from dto.Customer import Customer

result = CustomersDao.getAllCustomers()
print(result)

risultato_nomi = []
for customer in result:
    if len(customer.customerName) <= 6:
        risultato_nomi.append([customer.contactFirstName, customer.contactLastName])

        
    