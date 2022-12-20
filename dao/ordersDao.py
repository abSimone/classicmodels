from dao.utility.db import MySql

class Orders:

    @classmethod
    def getAllOrders(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM orders")
        data = MySql.getResults()
        MySql.closeConnection()
        return data

    @classmethod
    def getOrdersByCustomerNum(cls, num):
        MySql.openConnection()
        MySql.query(f"SELECT * \
                      FROM orders o \
                      INNER JOIN customers c ON o.customerNumber = c.customerNumber \
                      WHERE o.customerNumber={num}")
        data = MySql.getResults()
        MySql.closeConnection()
        return data

    @classmethod
    def getOrdersByOrderNum(cls, num):
        MySql.openConnection()
        MySql.query(f"SELECT * FROM orders WHERE orderNumber={num}")
        data = MySql.getResults()
        MySql.closeConnection()
        return data

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
                      WHERE productCode= '{code}' ")
        data = MySql.getResults()
        MySql.closeConnection()
        return data

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