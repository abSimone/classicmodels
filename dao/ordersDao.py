from dao.utility.db import MySql
from models.order import OrderModel
from dto.Order import Order


class Orders:

    @classmethod
    def getAllOrders(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM Orders")
        data = MySql.getResults()
        results = list()
        for element in data:
            results.append(OrderModel(orderNumber=element[0], orderDate=element[1], requiredDate=element[2], shippedDate=element[3], status=element[4], comments=element[5], customerNumber=element[6]))
        MySql.closeConnection()
        return results


    @classmethod
    def getOrdersByCustomerNum(cls, num):
        MySql.openConnection()
        MySql.query(f"SELECT o.orderNumber, o.orderDate, o.requiredDate, o.shippedDate, o.status, o.comments, o.customerNumber  \
                      FROM orders o \
                      INNER JOIN customers c ON o.customerNumber = c.customerNumber \
                      WHERE o.customerNumber={num}")
        data = MySql.getResults()
        allOrderds = []
        for element in data:
            allOrderds.append(Order(element[0], element[1], element[2], element[3], element[4], element[5], element[6]))
        MySql.closeConnection()
        return allOrderds[0]

    @classmethod
    def getOrdersByOrderNum(cls, num):
        MySql.openConnection()
        MySql.query(f"SELECT * FROM orders WHERE orderNumber={num}")
        data = MySql.getResults()
        allOrderds = []
        for element in data:
            allOrderds.append(Order(element[0], element[1], element[2], element[3], element[4], element[5], element[6]))
        MySql.closeConnection()
        return allOrderds[0]

    @classmethod
    def getOrdersByOrderStatus(cls, status):
        MySql.openConnection()
        MySql.query(f"SELECT * \
                      FROM orders o \
                      INNER JOIN customers c ON o.customerNumber = c.customerNumber \
                      WHERE status= '{status.capitalize()}' ") 
        data = MySql.getResults()
        MySql.closeConnection()
        return data

    @classmethod
    def getOrdersByCustomerCity(cls, city):
        MySql.openConnection()
        MySql.query(f"SELECT * \
                      FROM orders o \
                      INNER JOIN customers c ON o.customerNumber = c.customerNumber \
                      WHERE city= '{city.capitalize()}' ") 
        data = MySql.getResults()
        MySql.closeConnection()
        return data

    @classmethod
    def getOrdersByCustomerCountry(cls, country):
        MySql.openConnection()
        MySql.query(f"SELECT * \
                      FROM orders o \
                      INNER JOIN customers c ON o.customerNumber = c.customerNumber \
                      WHERE country= '{country.capitalize()}' ") 
        data = MySql.getResults()
        MySql.closeConnection()
        return data

    @classmethod
    def getOrdersByProductLineDate(cls, line):
        MySql.openConnection()
        MySql.query(f"SELECT * \
                      FROM orders \
                      INNER JOIN orderdetails on orderdetails.orderNumber=orders.orderNumber \
                      INNER JOIN products on orderdetails.productCode=products.productCode \
                      WHERE productLine= '{line}' and orderDate >= '2003-01-15' and orderDate <= '2003-01-31' ")
        data = MySql.getResults()
        MySql.closeConnection()
        return data

    @classmethod
    def getOrdersByProductCode(cls, code):
        MySql.openConnection()
        MySql.query(f"SELECT productName \
                      FROM orders \
                      INNER JOIN orderdetails on orderdetails.orderNumber=orders.orderNumber \
                      INNER JOIN products on orderdetails.productCode=products.productCode \
                      WHERE products.productCode= '{code}'")
        data = MySql.getResults()
        results = list()
        for element in data:
            results.append(Order(element[0], element[1], element[2], element[3], element[4], element[5], element[6]))
        MySql.closeConnection()
        return results

    @classmethod
    def getOrdersByProductLine(cls, line):
        MySql.openConnection()
        MySql.query(f"SELECT * \
                      FROM orders \
                      INNER JOIN orderdetails on orderdetails.orderNumber=orders.orderNumber \
                      INNER JOIN products on orderdetails.productCode=products.productCode \
                      WHERE productLine= '{line}' ")
        data = MySql.getResults()
        MySql.closeConnection()
        return data
    
    @classmethod
    def setOrder(cls, orderNumber, orderDate, requiredDate, shippedDate, status, comments, customerNumber):
        MySql.openConnection()
        MySql.query(f"insert  into orders(orderNumber,orderDate,requiredDate,shippedDate,status,comments,customerNumber) \
                      values  ({orderNumber},'{orderDate}','{requiredDate}','{shippedDate}','{status}',{comments},{customerNumber})")
        MySql.commit()
        MySql.closeConnection()

        