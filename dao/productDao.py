from dao.utility.db import MySql

class Product:

    @classmethod
    def getProductbyName(cls, product_name):
        MySql.openConnection()
        MySql.query(f'SELECT productLine, productName, cast(buyPrice as char) from products where productName="{product_name}" ') 
        data = MySql.getResults()
        for object in data:
            print(object)
        
        MySql.closeConnection()

    @classmethod
    def getProductbyProductline(cls, product_line):
        MySql.openConnection()
        MySql.query(f'SELECT productLine, productName, cast(buyPrice as char) from products where productLine="{product_line}" order by productName ') 
        data = MySql.getResults()
        for object in data:
            print(object)
        
        MySql.closeConnection()

    @classmethod
    def getAllProduct(cls):
        MySql.openConnection()
        MySql.query("SELECT productName, cast(buyPrice as char), cast(MSRP as char) from products order by productName") #inserisci query
        
        data = MySql.getResults()
        for object in data:
            print((object))
        
        MySql.closeConnection()

    
    @classmethod
    def  getProductbyID(cls, id_prodotto):
        MySql.openConnection()
        MySql.query(f'SELECT productCode, productName, cast(buyPrice AS char) FROM products WHERE productCode = "{id_prodotto}"') #inserisci query

        data=MySql.getResults()
        MySql.closeConnection()
        for object in data:
            print(object)
       
        MySql.closeConnection()
