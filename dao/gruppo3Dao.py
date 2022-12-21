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
    
    
    #Esercizio3
        
    @classmethod
    def getAllOrdersByEmployeeInfo(cls):
        first_name = input("\nEnter employee name: ")
        last_name = input("\nEnter employee surname: ")
        MySql.openConnection()
        MySql.query(f"SELECT * FROM Employees emp, Orders ord, Customers cus\
                        WHERE cus.customerNumber = ord.customerNumber and cus.salesRepEmployeeNumber = emp.employeeNumber\
                        and emp.firstName = '{first_name}' and emp.lastName = '{last_name}'")
        data = MySql.getResults()
        if data:  
            MySql.closeConnection()
            return data
        else:
            MySql.query(f"SELECT * FROM Employees")
            data = MySql.getResults()
            MySql.closeConnection()
            return data
    
    
    #Esercizio4
        
    @classmethod
    def getEmployeeAndOrdersInfoByCustomer(cls):
        first_name = input("\nEnter customer name: ")
        last_name = input("\nEnter customer surname: ")
        MySql.openConnection()
        MySql.query(f"SELECT emp.firstName, emp.lastName, count(*) FROM Orders ord, Employees emp, Customers cus\
                        WHERE cus.customerNumber = ord.customerNumber and cus.salesRepEmployeeNumber = emp.employeeNumber\
                        and cus.contactFirstName = '{first_name}' and cus.contactLastName = '{last_name}'\
                        GROUP BY emp.firstName, emp.lastName")
        data = MySql.getResults()
        if data:  
            MySql.closeConnection()
            return data
        else:
            MySql.query(f"SELECT * FROM Employees")
            data = MySql.getResults()
            MySql.closeConnection()
            return data