from dao.utility.db import MySql
from dto.productLine import ProductLine

class ProductLines:
    @classmethod
    def getAllProductLines(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM ProductLines")
        data = MySql.getResults()
        results = list()
        for element in data:
            results.append(ProductLine(element[0], element[1], element[2], element[3]))
        MySql.closeConnection()
        return results

    @classmethod
    def insertProductLine(cls, product_line, text_description):
        MySql.openConnection()
        MySql.query(f'insert into productLines values ("{product_line}","{text_description}" , null, null) ') 
        MySql.commit()
        MySql.closeConnection()

    @classmethod
    def deleteProductLine(cls, product_line):
        MySql.openConnection()
        MySql.query(f'DELETE FROM productlines WHERE productLine = "{product_line}"') 
        MySql.commit()
        MySql.closeConnection()

    
    @classmethod
    def  updateProductLine(cls, product_line, descrizione):
        MySql.openConnection()
        MySql.query(f'UPDATE productlines SET textDescription = "{descrizione}" WHERE productLine = "{product_line}"') 
        MySql.commit()
        MySql.closeConnection()