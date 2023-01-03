from dao.utility.db import MySql
from dto.Employee import Employee
from dto.Office import Office

class EmployeeDao:
    # read
    @classmethod
    def getAllEmployees(cls):
        MySql.openConnection()

        MySql.query("SELECT * FROM Employees")
        data = MySql.getResults()
        results = list()
        for element in data:
            results.append(Employee(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7]))

        MySql.closeConnection()
        return employees

    @classmethod
    def getEmployeeByNumber(cls, number):
        MySql.openConnection()
        MySql.query(f"select * from employees where employeeNumber = {number}")
        results = MySql.getResults()
        employee = Employee(results[0][0], results[0][1], results[0][2], results[0]
                            [3], results[0][4], results[0][5], results[0][6], results[0][7])
        MySql.closeConnection()
        return employee

    @classmethod
    def getEmployeesByCity(cls, city):
        MySql.openConnection()
        MySql.query(
            f"select * from employees INNER JOIN offices on employees.officeCode = offices.officeCode where offices.city = '{city}'")
        results = MySql.getResults()
        for item in results:
            data=Employee(item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7])
        MySql.closeConnection()

        return results
    
    @classmethod
    def getOfficeByEmployeeNumber(cls, employeeNumber):
        MySql.openConnection()
        MySql.query(
            f"select offices.officeCode,offices.city,offices.phone,offices.addressLine1,offices.addressLine2,offices.state,offices.country,offices.postalCode,offices.territory \
            from employees \
            INNER JOIN offices on employees.officeCode = offices.officeCode \
            where employees.employeeNumber = '{employeeNumber}'")
        results = MySql.getResults()
        data= list()
        for element in results:
            data.append(Office(element[0],element[1],element[2],element[3],element[4],element[5],element[6],element[7],element[8]))
        MySql.closeConnection()
        return data

    # Create
    # employee_data dev'essere un dict con le chiavi esplicitate per poter funzionare
    @classmethod
    def addEmployee(cls, employee_data):
        MySql.openConnection()
        MySql.query(
            f"INSERT INTO employees\
            VALUES(\
                {employee_data['employeeNumber']},\
                '{employee_data['lastName']}',\
                '{employee_data['firstName']}',\
                '{employee_data['extension']}',\
                '{employee_data['email']}',\
                {employee_data['officeCode']},\
                {employee_data['reportsTo']},\
                '{employee_data['jobTitle']}'\
            )")
        MySql.commit()
        MySql.closeConnection()

    # update
    @classmethod
    def updateEmployee(cls, employee_data):
        MySql.openConnection()
        MySql.query(
            f"update employees set lastName = '{employee_data['lastName']}', firstName =  '{employee_data['firstName']}', extension =  '{employee_data['extension']}', email = '{employee_data['email']}', officeCode = {employee_data['officeCode']}, reportsTo = {employee_data['reportsTo']}, jobTitle = '{employee_data['jobTitle']}' where employeeNumber = {employee_data['employeeNumber']}")
        MySql.commit()
        MySql.closeConnection()

    # delete
    @classmethod
    def removeEmployee(cls, employee_number):
        MySql.openConnection()
        MySql.query(
            f"delete from employees where employeeNumber = {employee_number}")
        MySql.commit()
        MySql.closeConnection()

    # dettagli ufficio di un impiegato
    @classmethod
    def getOfficeByEmployeeNumber(cls, employee_number):
        MySql.openConnection()
        MySql.query(
            f"select o.officeCode, o.city, o.phone, o.addressLine1, o.addressLine2, o.state, o.country, o.postalCode, o.territory \
            from employees e \
            INNER JOIN offices o on e.officeCode=o.officeCode \
            where employeeNumber={employee_number}")
        results = MySql.getResults()
        office = Office(results[0][0], results[0][1], results[0][2], results[0][3],
                        results[0][4], results[0][5], results[0][6], results[0][7], results[0][8])
        MySql.closeConnection()
        return office
