from dao.utility.db import MySql
from models.product import ProductModel
from dto.Product import Products


class Product:

    @classmethod
    def getProductbyName(cls, product_name):
        MySql.openConnection()
        MySql.query(
            f'SELECT productLine, productName, cast(buyPrice as char) from products where productName="{product_name}" ')
        data = MySql.getResults()
        product = Products(data[0][0], data[0][1], data[0][2], data[0][3], data[0][4],
                           data[0][5], data[0][6], data[0][7], data[0][8])

        MySql.closeConnection()
        return product

    @classmethod
    def getProductbyProductline(cls, product_line):
        MySql.openConnection()
        MySql.query(
            f'SELECT productLine, productName, cast(buyPrice as char) from products where productLine="{product_line}" order by productName ')
        data = MySql.getResults()
        products = []
        for object in data:
            products.append(Product(object[0], object[1], object[2], object[3], object[4],
                                     object[5], object[6], object[7], object[8]))

        MySql.closeConnection()

    @classmethod
    def getAllProduct(cls):
        MySql.openConnection()
        MySql.openConnection()
        MySql.query("SELECT * FROM products")
        data = MySql.getResults()
        results = list()
        for element in data:
            results.append(ProductModel(productCode= element[0], productName= element[1], productLine= element[2], productScale= element[3], productVendor= element[4], productDescription= element[5], quantityInStock= element[6], buyPrice= element[7], MSRP= element[8]))
        MySql.closeConnection()
        return results

    @classmethod
    def getProductbyID(cls, id_prodotto):
        MySql.openConnection()
        # inserisci query
        MySql.query(
            f'SELECT productCode, productName, cast(buyPrice AS char) FROM products WHERE productCode = "{id_prodotto}"')

        data = MySql.getResults()
        MySql.closeConnection()
        product = Products(data[0][0], data[0][1], data[0][2], data[0][3], data[0][4],
                           data[0][5], data[0][6], data[0][7], data[0][8])
        MySql.closeConnection()
        return product

    @classmethod
    def insertProduct(cls, product_code, product_name, product_line, product_scale, product_vendor, product_description, quantity_instock, buy_price, msrp):
        MySql.openConnection()
        MySql.query(f'insert  into products(productCode,productName,productLine,productScale,productVendor,productDescription,quantityInStock,buyPrice,MSRP)\
                    values ("{product_code}","{product_name}","{product_line}","{product_scale}","{product_vendor}","{product_description}","{quantity_instock}","{buy_price}","{msrp}")')
        MySql.commit()
        MySql.closeConnection()
