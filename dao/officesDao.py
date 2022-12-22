from dao.utility.db import MySql
from dto.Offices import Offices


class OfficeDao:
    # read
    @classmethod
    def getAllOffices(cls):
        MySql.openConnection()
        MySql.query("select * from offices")
        results = MySql.getResults()
        MySql.closeConnection()
        return results
    
    @classmethod
    def getOfficeByEmployeeNum(cls, employee_num):
        MySql.openConnection()
        MySql.query(f"SELECT o.officeCode, city, phone, addressLine1, addressLine2, state, country, postalCode, territory \
                    FROM offices o \
                    INNER JOIN employees e on o.officeCode = e.officeCode \
                    WHERE e.employeeNumber=\"{employee_num}\"")
        results = MySql.getResults()
        data=list()
        # for item in results:
        data.append(Offices(results[0][0],results[0][1],results[0][2],results[0][3],results[0][4],results[0][5],results[0][6],results[0][7],results[0][8]))
        MySql.closeConnection()
        return data
    

    # Create
    # office_data dev'essere un dict con le chiavi esplicitate per poter funzionare
    @classmethod
    def addOffice(cls, office_data):
        MySql.openConnection()
        MySql.query(
            f"INSERT INTO offices\
            VALUES(\
                {office_data['officeCode']},\
                {office_data['city']},\
                '{office_data['phone']}',\
                '{office_data['addressLine1']}',\
                '{office_data['addressLine2']}',\
                '{office_data['state']}',\
                {office_data['country']},\
                '{office_data['postalCode']}'\
                '{office_data['territory']}'\
            )")
        MySql.commit()
        MySql.closeConnection()

    # update
    @classmethod
    def updateOffice(cls, office_data):
        MySql.openConnection()
        MySql.query(
            f"update offices set city = '{office_data['city']}', phone ='{office_data['phone']}', addressLine1 =  '{office_data['addressLine1']}', addressLine2 = '{office_data['addressLine2']}', state = {office_data['state']}, country = '{office_data['country']}', postalCode = '{office_data['postalCode']}' territory = '{office_data['territory']}' where officeCode = {office_data['officeCode']}")
        MySql.commit()
        MySql.closeConnection()

    # delete
    @classmethod
    def removeOffice(cls, office_code):
        MySql.openConnection()
        MySql.query(
            f"delete from offices where officeCode = {office_code}")
        MySql.commit()
        MySql.closeConnection()
