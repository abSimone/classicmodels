from dao.utility.db import MySql
from models.productLines import ProductLinesModel

from dto.ProductLines import ProductsLines


class ProductLines:
    @classmethod
    def getAllProductLines(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM productlines")
        data = MySql.getResults()

        results = list()
        for element in data:
            results.append(ProductLinesModel(productLine= element[0], textDescription= element[1], htmlDescription= element[2], image= element[3]))
        MySql.closeConnection()
        return results
    
    @classmethod
    def getProductLineByPrimaryKey(cls, productLine):
        MySql.openConnection()
        MySql.query(f"SELECT * from productlines where productLine = '{productLine}'") 
        data = MySql.getResults()
        product = ProductsLines(data[0][0], data[0][1],data[0][2],data[0][3])
        MySql.closeConnection()
        return product


    @classmethod
    def insertProductLine(cls, product_line, text_description):
        MySql.openConnection()
        MySql.query(f'insert into productlines values ("{product_line}","{text_description}" , null, null) ') 
        MySql.commit()

        MySql.closeConnection()

    @classmethod
    def deleteProductLine(cls, product_line):
        MySql.openConnection()
        MySql.query(f'DELETE FROM productlines WHERE productLine = "{product_line}"') 
        MySql.commit()

        MySql.closeConnection()

    
    @classmethod
    def updateProductLine(cls, product_line, descrizione):
        MySql.openConnection()
        MySql.query(f'UPDATE productlines SET textDescription = "{descrizione}" WHERE productLine = "{product_line}"') 
        MySql.commit()

        MySql.closeConnection()