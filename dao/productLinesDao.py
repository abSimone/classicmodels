from dao.utility.db import MySql

class ProductLines:
    @classmethod
    def getAllProductLines(cls):
        MySql.openConnection()
        MySql.query(f'SELECT * from productLines ') 
        data = MySql.getResults()
        for object in data:
            print(object)
        
        MySql.closeConnection()

    @classmethod
    def insertProductLine(cls, product_line, text_description):
        MySql.openConnection()
        MySql.query(f'insert into productLines values ("{product_line}","{text_description}" , null, null) ') 
        MySql.dbCommit
        
        MySql.closeConnection()

    @classmethod
    def getAllProduct(cls, product_line):
        MySql.openConnection()
        MySql.query(f'DELETE FROM productlines WHERE productLine = "{product_line}"') 
        MySql.dbCommit()
        
        MySql.closeConnection()

    
    @classmethod
    def  getProductbyID(cls, product_line, descrizione):
        MySql.openConnection()
        MySql.query(f'UPDATE productlines SET textDescription = "{descrizione}" WHERE productLine = "{product_line}"') 
        MySql.dbCommit()
       
        MySql.closeConnection()