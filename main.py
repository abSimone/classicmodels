from dao.EmployeeDao import EmployeeDao
from dto.Office import Office

employeeNumber1 =int(input("Inserisci un codice dell'employee : "))
result=EmployeeDao.getOfficeByEmployeeNumber(employeeNumber1)

Uffici=[]
for element in result:
    Uffici.append(element.officeCode)
    
print(Uffici)


        
    