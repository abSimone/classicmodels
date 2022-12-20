from dao.utility.db import MySql

class Risoluzione:
    @classmethod
    def getCustomerbyOfficecode(cls, office_code):
        MySql.openConnection()
        MySql.query(f'SELECT c.customerName from employees e inner join customers c on c.salesRepEmployeeNumber=e.employeeNumber inner join offices o on o.officeCode=e.officeCode where e.officeCode="{office_code}" ') 
        data = MySql.getResults()
        for object in data:
            print(object)
        
        MySql.closeConnection()

    @classmethod
    def getOrdersbyProductline(cls, product_line):
        MySql.openConnection()
        MySql.query(f'select o.orderNumber, orderDate, requiredDate, shippedDate, status from orders o inner join orderdetails od on o.orderNumber=od.orderNumber inner join products p on p.productCode=od.productCode inner join productlines pl on p.productLine=pl.productLine where p.productLine=\'{product_line}\' and orderDate between \'2003-01-15\' and \'2003-01-31\'')
        data = MySql.getResults()
        for object in data:
            print(object)
        
        MySql.closeConnection()

    @classmethod
    def getOrdersbyEmployee(cls, nome, cognome):
        MySql.openConnection()
        MySql.query(f'select e.employeeNumber, e.firstName, e.lastName, e.officeCode, e.email from employees e \
            inner join customers c on e.employeeNumber=c.salesRepEmployeeNumber\
            inner join orders o on o.customerNumber=c.customerNumber\
            where e.firstName="{nome}" and e.lastName="{cognome}"')
        print('Lista ordini:\n')
        MySql.query(f'select o.orderNumber from employees e \
            inner join customers c on e.employeeNumber=c.salesRepEmployeeNumber\
            inner join orders o on o.customerNumber=c.customerNumber\
            where e.firstName="{nome}" and e.lastName="{cognome}"')
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