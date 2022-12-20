from dao.utility.db import MySql

class CustomersDao:
    @classmethod
    def getAllCustomers(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM Customers")
        data = MySql.getResults()
        MySql.closeConnection()
        return data
    
    @classmethod
    def getAllCustomerNumber(cls):
        MySql.openConnection()
        MySql.query("SELECT customerNumber FROM customers")
        data= MySql.getResults()
        MySql.closeConnection()
        
        return data
    
    @classmethod
    def getAllCustomersName(cls):
        MySql.openConnection()
        MySql.query("SELECT customerName FROM customers")
        data= MySql.getResults()
        MySql.closeConnection()
        
        return data
    
    @classmethod
    def getAllContactLastName(cls):
        MySql.openConnection()
        MySql.query("SELECT contactLastName FROM customers")
        data= MySql.getResults()
        MySql.closeConnection()
        
        return data
    
    @classmethod
    def getAllContactFirstName(cls):
        MySql.openConnection()
        MySql.query("SELECT contactFirstName FROM customers")
        data= MySql.getResults()
        MySql.closeConnection()
        
        return data
    
    @classmethod
    def getAllContact(cls):
        MySql.openConnection()
        MySql.query("SELECT contactFirstName,contactLastName FROM customers")
        data= MySql.getResults()
        MySql.closeConnection()
        
        return data
    
    
    @classmethod
    def getAllPhone(cls):
        MySql.openConnection()
        MySql.query("SELECT phone FROM customers")
        data= MySql.getResults()
        MySql.closeConnection()
        
        return data
    
    @classmethod
    def getAllAddressLine(cls):
        MySql.openConnection()
        MySql.query("SELECT addressLine1,addressLine2 FROM customers")
        data= MySql.getResults()
        MySql.closeConnection()
        
        return data
    
    @classmethod
    def getAllPosition(cls):
        MySql.openConnection()
        MySql.query("SELECT city,state,postalCode,country FROM customers")
        data= MySql.getResults()
        MySql.closeConnection()
        
        return data
    
    @classmethod
    def getAllNameLondon(cls):
        MySql.openConnection()
        MySql.query("select c.contactLastName, c.contactFirstName from customers as c where c.city = 'London'")
        data= MySql.getResults()
        MySql.closeConnection()
        
        return data
    
    @classmethod
    def getAllOrdersByCustomerNumber(cls):
        value = int(input("\nEnter the customer number: "))
        MySql.openConnection()
        MySql.query(f"SELECT * FROM Orders ord JOIN Customers cus on ord.customerNumber = cus.customerNumber WHERE cus.customerNumber = {value}")
        data = MySql.getResults()
        MySql.closeConnection()
        return data
    
    @classmethod
    def getAllPaymentsByCustomerNumber(cls):
        value = int(input("\nEnter the customer number: "))
        MySql.openConnection()
        MySql.query(f"SELECT * FROM Payments pay JOIN Customers cus on pay.customerNumber = cus.customerNumber WHERE cus.customerNumber = {value}")
        data = MySql.getResults()
        MySql.closeConnection()
        return data
    
    @classmethod
    def getAllEmployeesBySalesRepEmployeeNumber(cls):
        value = int(input("\nEnter the sales rep employee number: "))
        MySql.openConnection()
        MySql.query(f"SELECT * FROM Employees emp JOIN Customers cus on emp.employeeNumber = cus.salesRepEmployeeNumber WHERE cus.salesRepEmployeeNumber = {value}")
        data = MySql.getResults()
        MySql.closeConnection()
        return data