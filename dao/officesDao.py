from dao.utility.db import MySql
from dto.office import Office

class OfficeDao:
    # read
    @classmethod
    def getAllOffices(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM Offices")
        data = MySql.getResults()
        results = list()
        for element in data:
            results.append(Office(element[0], element[1], element[2], element[3], element[4], element[5], element[6]))
        MySql.closeConnection()
        return results

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
