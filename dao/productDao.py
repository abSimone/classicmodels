from dao.utility.db import MySql
from dto.productdto import Productdto

class Product:

    @classmethod
    def getProductbyName(cls, product_name):
        MySql.openConnection()
        MySql.query(f'SELECT productLine, productName, cast(buyPrice as char) from products where productName="{product_name}" ') 
        data = MySql.getResults()
        product=list()
        for element in data:
            product.append(Productdto(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7], element[8]))
        MySql.closeConnection()
        return product

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
            print(object)
        
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
    
    @classmethod
    def insertProduct(cls, product_code, product_name, product_line, product_scale, product_vendor, product_description, quantity_instock, buy_price, msrp):
        MySql.openConnection()
        MySql.query(f'insert  into products(productCode,productName,productLine,productScale,productVendor,productDescription,quantityInStock,buyPrice,MSRP)\
                    values ("{product_code}","{product_name}","{product_line}","{product_scale}","{product_vendor}","{product_description}","{quantity_instock}","{buy_price}","{msrp}")')
        MySql.commit()
        MySql.closeConnection()
