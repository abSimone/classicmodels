from dao.utility.db import MySql
from dto.OrderDetails import OrderDetails

class orderDetails:

    @classmethod
    def getAllOrdersDetails(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM orderdetails")
        data = MySql.getResults()
        orderdt=list()
        for element in data:
            orderdt.append(OrderDetails(element[0], element[1], element[2], element[3], element[4]))
        MySql.closeConnection()
        return orderdt

    @classmethod
    def getAllOrdersDetailsNumber(cls):
        MySql.openConnection()
        MySql.query("SELECT orderNumber FROM orderdetails")
        data = MySql.getResults()
        MySql.closeConnection()
        return data

    @classmethod
    def getAllOrdersDetailsByStatus(cls, status):
        MySql.openConnection()
        MySql.query(f"SELECT * \
                     FROM orderDetails od \
                     INNER JOIN Orders o ON od.orderNumber = o.orderNumber \
                     WHERE status = '{status}' ")
        data = MySql.getResults()
        MySql.closeConnection()
        return data

    @classmethod
    def getAllOrdersDetailsByOrderNumber(cls, orderNumber):
        MySql.openConnection()
        MySql.query(f"SELECT * \
                     FROM orderDetails od \
                     INNER JOIN Orders o ON od.orderNumber = o.orderNumber \
                     WHERE od.orderNumber = '{orderNumber}' ")
        data = MySql.getResults()
        MySql.closeConnection()
        return data

    @classmethod
    def getAllOrdersDetailsByCustomerNumber(cls, Cnum):
        MySql.openConnection()
        MySql.query(f"SELECT * \
                     FROM orderDetails od \
                     INNER JOIN Orders o ON od.orderNumber = o.orderNumber \
                     WHERE o.customerNumber = '{Cnum}' ")
        data = MySql.getResults()
        MySql.closeConnection()
        return data

    @classmethod
    def getAllOrdersDetailsByOrderLineNumber(cls, Odnum):
        MySql.openConnection()
        MySql.query(f"SELECT * \
                     FROM orderDetails od \
                     INNER JOIN Orders o ON od.orderNumber = o.orderNumber \
                     WHERE od.orderLineNumber = '{Odnum}' ")
        data = MySql.getResults()
        MySql.closeConnection()
        return data

    @classmethod
    def getAllOrdersDetailsByProductCode(cls, code):
        MySql.openConnection()
        MySql.query(f"SELECT * \
                      FROM orderDetails od \
                      INNER JOIN Products p ON od.productCode = p.productCode \
                      WHERE p.productCode = '{code}' ")
        data = MySql.getResults()
        MySql.closeConnection()
        return data

    @classmethod
    def getAllOrdersDetailsByProductLine(cls, productLine):
        MySql.openConnection()
        MySql.query(f"SELECT * \
                      FROM orderDetails od \
                      INNER JOIN Products p ON od.productCode = p.productCode \
                      WHERE productLine = '{productLine}' ")
        data = MySql.getResults()
        MySql.closeConnection()
        return data

    @classmethod
    def getAllOrdersDetailsByProductVendor(cls, productVendor):
        MySql.openConnection()
        MySql.query(f"SELECT * \
                      FROM orderDetails od \
                      INNER JOIN Products p ON od.productCode = p.productCode \
                      WHERE productVendor = '{productVendor}' ")
        data = MySql.getResults()
        MySql.closeConnection()
        return data

    @classmethod
    def getAllOrdersDetailsByProductVendor(cls, productVendor):
        MySql.openConnection()
        MySql.query(f"SELECT * \
                      FROM orderDetails od \
                      INNER JOIN Products p ON od.productCode = p.productCode \
                      WHERE productVendor = '{productVendor}' ")
        data = MySql.getResults()
        MySql.closeConnection()
        return data

    @classmethod
    def getAllOrdersDetailsByPriceMax(cls, priceMax):
        MySql.openConnection()
        MySql.query(f"SELECT * \
                      FROM orderDetails od \
                      INNER JOIN Products p ON od.productCode = p.productCode \
                      WHERE od.priceEach >= '{priceMax}' \
                      GROUP BY p.productName ")
        data = MySql.getResults()
        MySql.closeConnection()
        return data

    @classmethod
    def getAllOrdersDetailsByPriceMin(cls, priceMin):
        MySql.openConnection()
        MySql.query(f"SELECT * \
                      FROM orderDetails od \
                      INNER JOIN Products p ON od.productCode = p.productCode \
                      WHERE od.priceEach <= '{priceMin}' \
                      GROUP BY p.productName ")
        data = MySql.getResults()
        MySql.closeConnection()
        return data



    
