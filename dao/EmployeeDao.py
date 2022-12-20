from dao.utility.db import MySql

class EmployeeDao:
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
        MySql.query(f"select * from employees INNER JOIN offices on employees.officeCode = offices.officeCode where offices.city = '{city}'")
        results = MySql.getResults()
        MySql.closeConnection()
        return results


