from dao.EmployeeDao import EmployeeDao

employeeNumber1 =int(input("Inserisci un codice dell'employee : "))
result=EmployeeDao.getOfficeByEmployeeNumber(employeeNumber1)
print(result)


        
    