from dao.utility.db import MySql

class PaymentsDao:
    @classmethod
    def getAllPayments(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM payments")
        data = MySql.getResults()
        MySql.closeConnection()
        return data
    
    @classmethod
    def getAllCheckNumbers(cls):
        MySql.openConnection()
        MySql.query("SELECT checkNumber FROM payments")
        data= MySql.getResults()
        MySql.closeConnection()
        
        return data
    
    @classmethod
    def getAllDates(cls):
        MySql.openConnection()
        MySql.query("SELECT paymentDate FROM payments")
        data= MySql.getResults()
        MySql.closeConnection()
        
        return data
    
    @classmethod
    def getAllAmount(cls):
        MySql.openConnection()
        MySql.query("SELECT amount FROM payments")
        data= MySql.getResults()
        MySql.closeConnection()
        
        return data
    
    @classmethod
    def getAllPaymentsCustomer(cls):
        customerNumber = int(input('Enter a customer number:\n'))
        MySql.openConnection()
        MySql.query(f"SELECT COUNT(*) FROM payments pay \
                    JOIN customers cus on  pay.customerNumber = cus.customerNumber\
                    WHERE cus.customerNumber = {customerNumber}")
        data= MySql.getResults()
        MySql.closeConnection()
        
        return data
    
    @classmethod
    def getAllDatePaymentsCountry(cls):
        minDate = input('Enter a min date:\n')
        maxDate = input('Enter a max date:\n')
        country = input('Enter a country: \n')
        MySql.openConnection()
        MySql.query(f"SELECT * \
                    FROM payments pay \
                    JOIN customers cus on  pay.customerNumber = cus.customerNumber \
                    WHERE pay.paymentDate between '{minDate}' and '{maxDate}' \
                    and cus.country = '{country}'")
        data= MySql.getResults()
        MySql.closeConnection()
        
        return data
        
    