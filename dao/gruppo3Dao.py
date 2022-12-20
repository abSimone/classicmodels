from dao.utility.db import MySql

class Gruppo3Dao:
    
    #Esercizio1
    
    @classmethod
    def getAllCustomersByOfficeCode(cls):
        value = int(input("\nEnter office code: "))
        MySql.openConnection()
        MySql.query(f"SELECT * FROM Customers cus JOIN Employees emp on cus.salesRepEmployeeNumber = emp.employeeNumber WHERE emp.officeCode = {value}")
        data = MySql.getResults()
        MySql.closeConnection()
        return data
    
    
    #Esercizio2
    
    @classmethod
    def getAllOrdersByProductLine(cls):
        value = input("\nEnter product line: ")
        MySql.openConnection()
        MySql.query(f"SELECT * FROM Orders ord\
                        JOIN Orderdetails ordde on ord.orderNumber = ordde.orderNumber\
                        JOIN Products pro on pro.productCode = ordde.productCode\
                        WHERE pro.productLine = '{value}' and ord.orderDate between '2003-01-15' and '2003-01-31'")
        data = MySql.getResults()
        MySql.closeConnection()
        return data