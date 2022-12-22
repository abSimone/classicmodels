from dao.utility.db import MySql
from dto.Customer import Customer

class CustomersDao:
    @classmethod
    def getCustomerByCustomerNumber(cls, customerNumber):
        MySql.openConnection()
        MySql.query(f"SELECT cus.contactFirstName, cus.contactLastName FROM customers cus WHERE cus.customerNumber = '{customerNumber}'")
        data= MySql.getResults()
        MySql.closeConnection()
        
        return data
    
    @classmethod
    def getAllCustomers(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM Customers")
        data = MySql.getResults()
        results = list()
        for element in data:
            results.append(Customer(element[0], element[1], element[2], element[3], element[4], element[5]))
        MySql.closeConnection()
        return results

    
    @classmethod
    def getAllNameLondon(cls):
        MySql.openConnection()
        MySql.query("select c.contactLastName, c.contactFirstName from customers as c where c.city = 'London'")
        data= MySql.getResults()
        MySql.closeConnection()
        
        return data
    
    @classmethod
    def getAllOrdersByCustomerNumber(cls, customerNumber):
        MySql.openConnection()
        MySql.query(f"SELECT * FROM Orders ord JOIN Customers cus on ord.customerNumber = cus.customerNumber WHERE cus.customerNumber = {customerNumber}")
        data = MySql.getResults()
        MySql.closeConnection()
        return data
    
    @classmethod
    def getAllPaymentsByCustomerNumber(cls, customerNumber):
        MySql.openConnection()
        MySql.query(f"SELECT * FROM Payments pay JOIN Customers cus on pay.customerNumber = cus.customerNumber WHERE cus.customerNumber = {customerNumber}")
        data = MySql.getResults()
        MySql.closeConnection()
        return data
    
    # insert
    @classmethod
    def insertCustomer(cls, customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit):
        print("\nAdd new customer")
        MySql.openConnection()
        MySql.query(f"INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit)\
                        VALUES ('{customerNumber}', '{customerName}', '{contactLastName}', '{contactFirstName}', '{phone}', '{addressLine1}', '{addressLine2}', '{city}', '{state}', '{postalCode}', '{country}', '{salesRepEmployeeNumber}', '{creditLimit}')")
        MySql.commit()
        MySql.closeConnection()
        
    # delete
    @classmethod
    def deleteCustomer(cls, customerNumber):
        MySql.openConnection()
        MySql.query("SET FOREIGN_KEY_CHECKS=0")
        MySql.query(f"DELETE from customers where customerNumber = {customerNumber}")
        MySql.query("SET FOREIGN_KEY_CHECKS=1")
        MySql.commit()
        MySql.closeConnection()
        
    # update
    @classmethod
    def insertCustomer(cls, customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, creditLimit):
        print("\nUpdate Customer")
        MySql.openConnection()
        MySql.query(f"UPDATE customers\
                    SET customerName = '{customerName}', contactLastName = '{contactLastName}', \
                    contactFirstName = '{contactFirstName}', phone = {phone}, addressLine1 = '{addressLine1}', addressLine2 = '{addressLine2}', \
                    city = '{city}', state = '{state}', postalCode = {postalCode}, country = '{country}', creditLimit = {creditLimit} \
                    WHERE customerNumber = {customerNumber}")
        MySql.commit()
        MySql.closeConnection()
        
        