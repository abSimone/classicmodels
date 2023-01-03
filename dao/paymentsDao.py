from dao.utility.db import MySql
from dto.Payment import Payment

class PaymentsDao:
    @classmethod
    def getAllPayments(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM Payments")
        data = MySql.getResults()
        results = list()
        for element in data:
            results.append(Payments(element[0], element[1], element[2], element[3]))
        MySql.closeConnection()
        return results
    
    @classmethod
    def getPaymentByCheckNumber(cls, checkNumber):
        MySql.openConnection()
        MySql.query(f"SELECT * FROM payments where checkNumber = '{checkNumber}'")
        data = MySql.getResults()
        payment = Payment(data[0][0], data[0][1], data[0][2], data[0][3])
        MySql.closeConnection()
        return payment
    
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
    def getPaymentBYCustomerNumber(cls, customerNumber):
        MySql.openConnection()
        MySql.query(f'SELECT p.checkNumber, p.paymentDate, p.amount \
                        FROM payments p\
                        INNER JOIN customers c ON p.customerNumber = c.customerNumber\
                        WHERE c.customerNumber = {customerNumber}')
        data= MySql.getResults()
        MySql.closeConnection()
        
        return data
    
    @classmethod
    def getAllDatePaymentsCountry(cls,minDate,maxDate,country):
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
    def insertPayment(cls, customerNumber, checkNumber, paymentDate, amount):
        MySql.openConnection()
        MySql.query(f"INSERT INTO payments (customerNumber, checkNumber, paymentDate, amount)\
                        VALUES ({customerNumber}, '{checkNumber}', '{paymentDate}', {amount})")
        MySql.commit()
        MySql.closeConnection()
    
    # update
    @classmethod
    def updatePayment(cls, checkNumber, paymentDate, amount):
        MySql.openConnection()
        MySql.query(f"UPDATE payments\
                    SET paymentDate = '{paymentDate}', amount = {amount} \
                    WHERE checkNumber = '{checkNumber}'")
        MySql.commit()
        MySql.closeConnection()
        
    # delete
    @classmethod
    def deletePayment(cls, checkNumber):
        MySql.openConnection()
        MySql.query("SET FOREIGN_KEY_CHECKS=0")
        MySql.query(f"DELETE from payments where checkNumber = '{checkNumber}'")
        MySql.query("SET FOREIGN_KEY_CHECKS=1")
        MySql.commit()
        MySql.closeConnection()
        
        
    