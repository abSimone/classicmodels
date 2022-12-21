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
    
    # insert
    @classmethod
    def insertPayment(cls):
        print("\nAdd new payment")
        customerNumber = int(input("\nEnter the customer number: "))
        checkNumber = input("\nEnter the check number: ")
        paymentDate = input("\nEnter the payment date: ")
        amount = float(input("\nEnter the amount: "))
        MySql.openConnection()
        MySql.query(f"INSERT INTO payments (customerNumber, checkNumber, paymentDate, amount)\
                        VALUES ({customerNumber}, '{checkNumber}', '{paymentDate}', {amount})")
        MySql.commit()
        MySql.closeConnection()
    
    # update
    @classmethod
    def updatePayment(cls):
        print("\nUpdate payment")
        checkNumber = input('\nEnter the checkNumber:')
        paymentDate = input("\nEnter the payment date: ")
        amount = float(input("\nEnter the amount: "))
        MySql.openConnection()
        MySql.query(f"UPDATE payments\
                    SET paymentDate = '{paymentDate}', amount = {amount} \
                    WHERE checkNumber = '{checkNumber}'")
        MySql.commit()
        MySql.closeConnection()
        
    # delete
    @classmethod
    def deletePayment(cls):
        value = input("Enter the checknumber of the payment you want to delete: ")
        MySql.openConnection()
        MySql.query("SET FOREIGN_KEY_CHECKS=0")
        MySql.query(f"DELETE from payments where checkNumber = '{value}'")
        MySql.query("SET FOREIGN_KEY_CHECKS=1")
        MySql.commit()
        MySql.closeConnection()
        
        
    