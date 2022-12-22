from dao.officesDao import OfficeDao
from dto.Customer import Customer
from dao.EmployeeDao import EmployeeDao

result = EmployeeDao.getAllEmployees()
for i in result:
    print(i)


        
    