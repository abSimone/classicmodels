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
    
    @classmethod
    def insertCustomer(cls):
        print("\nAdd new customer")
        customerNumber = int(input("\nEnter the customer number: "))
        customerName = input("\nEnter the customer name: ")
        contactLastName = input("\nEnter the customer first name: ")
        contactFirstName = input("\nEnter the customer last name: ")
        phone = int(input("\nEnter the customer phone number: "))
        addressLine1 = input("\nEnter address 1: ")
        addressLine2 = input("\nEnter address 2: ")
        city = input("\nEnter city: ")
        state = input("\nEnter state: ")
        postalCode = int(input("\nEnter postal code: "))
        country = input("\nEnter country: ")
        salesRepEmployeeNumber = int(input("\nEnter employee number: "))
        creditLimit = int(input("\nEnter credit limit: "))
        MySql.openConnection()
        MySql.query(f"INSERT INTO Customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit)\
                        VALUES ('{customerNumber}', '{customerName}', '{contactLastName}', '{contactFirstName}', '{phone}', '{addressLine1}', '{addressLine2}', '{city}', '{state}', '{postalCode}', '{country}', '{salesRepEmployeeNumber}', '{creditLimit}')")
        MySql.commit()
        MySql.closeConnection()
        return
    
    @classmethod
    def deleteCustomer(cls):
        value = input("Enter the customer number you want delete: ")
        MySql.openConnection()
        MySql.query(f"DELETE FROM Customers WHERE customerNumber={value}")
        MySql.commit()
        MySql.closeConnection()
        return