from dao.EmployeeDao import EmployeeDao
from dto.Office import Office

employeeNumber1 =int(input("Inserisci un codice dell'employee : "))
result=EmployeeDao.getOfficeByEmployeeNumber(employeeNumber1)

for e in result:
    print(e)



        
    