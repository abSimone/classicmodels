from dao.utility.db import MySql
from dto.Employee import Employee


class EmployeeDao:
    # read
    @classmethod
    def getAllEmployees(cls):
        MySql.openConnection()
        MySql.query("select * from employees")
        results = MySql.getResults()
        data=list()
        for item in results:
            data.append(Employee(item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7]))
        MySql.closeConnection()
        return data

    @classmethod
    def getEmployeeByNumber(cls, number):
        MySql.openConnection()
        MySql.query(f"select * from employees where employeeNumber = {number}")
        results = MySql.getResults()
        for item in results:
            data=Employee(item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7])
        MySql.closeConnection()
        return data

    @classmethod
    def getEmployeesByCity(cls, city):
        MySql.openConnection()
        MySql.query(
            f"select * from employees INNER JOIN offices on employees.officeCode = offices.officeCode where offices.city = '{city}'")
        results = MySql.getResults()
        for item in results:
            data=Employee(item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7])
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
