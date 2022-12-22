from dao.utility.db import MySql
from dto.productlinesdto import ProductLinesdto

class ProductLines:
    @classmethod
    def getAllProductLines(cls):
        MySql.openConnection()
        MySql.query(f'SELECT * from productLines ') 
        data = MySql.getResults()
        productline=list()
        for element in data:
            productline.append(ProductLinesdto(element[0], element[1], element[2], element[3]))
        MySql.closeConnection()
        return productline

    @classmethod
    def insertProductLine(cls, product_line, text_description):
        MySql.openConnection()
        MySql.query(f'insert into productLines values ("{product_line}","{text_description}" , null, null) ') 
        MySql.dbCommit
        
        MySql.closeConnection()

    @classmethod
    def deleteProductLine(cls, product_line):
        MySql.openConnection()
        MySql.query(f'DELETE FROM productlines WHERE productLine = "{product_line}"') 
        MySql.dbCommit()
        
        MySql.closeConnection()

    
    @classmethod
    def  updateProductLine(cls, product_line, descrizione):
        MySql.openConnection()
        MySql.query(f'UPDATE productlines SET textDescription = "{descrizione}" WHERE productLine = "{product_line}"') 
        MySql.dbCommit()
       
        MySql.closeConnection()