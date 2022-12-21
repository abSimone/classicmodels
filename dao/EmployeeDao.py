from dao.utility.db import MySql


class EmployeeDao:
    # read
    @classmethod
    def getAllEmployees(cls):
        MySql.openConnection()
        MySql.query("select * from employees")
        results = MySql.getResults()
        MySql.closeConnection()
        return results

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
            f"update employees set lastName =  '{employee_data['lastName']}', firstName =  '{employee_data['firstName']}' where employeeNumber = {employee_data['employeeNumber']}")
        MySql.commit()
        MySql.closeConnection()

    # delete employee
    @classmethod
    def removeEmployee(cls, employee_number):
        MySql.openConnection()
        MySql.query(
            f"delete from employees where employeeNumber = {employee_number}")
        MySql.commit()
        MySql.closeConnection()
