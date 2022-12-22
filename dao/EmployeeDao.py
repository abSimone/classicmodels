from dao.utility.db import MySql
from dto.emplyeedto import Employeedto

class EmployeeDao:
    # read
    @classmethod
    def getAllEmployees(cls):
        MySql.openConnection()
        MySql.query("select * from employees")
        results = MySql.getResults()
        employee=list()
        for element in results:
            employee.append(Employeedto(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7]))
        MySql.closeConnection()
        return employee

    @classmethod
    def getEmployeeByNumber(cls, number):
        MySql.openConnection()
        MySql.query(f"select * from employees where employeeNumber = {number}")
        results = MySql.getResults()
        MySql.closeConnection()
        return results

    @classmethod
    def getEmployeesByCity(cls, city):
        MySql.openConnection()
        MySql.query(
            f"select * from employees INNER JOIN offices on employees.officeCode = offices.officeCode where offices.city = '{city}'")
        results = MySql.getResults()
        MySql.closeConnection()
        return results

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
