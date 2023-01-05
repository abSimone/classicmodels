from dao.utility.db import MySql
from dto.Office import Office
from models.office import OfficeModel

class OfficeDao:
    # read
    @classmethod
    def getAllOffices(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM Offices")
        data = MySql.getResults()
        results = list()
        for element in data:
            print(element)
            results.append(OfficeModel(officeCode = element[0], city = element[1], phone = element[2], addressLine1 = element[3], addressLine2 = element[4], state = element[5], country = element[6], postalCode = element[7], territory = element[8]))
        MySql.closeConnection()

        return results
    
    @classmethod
    def getOfficeByOfficeCode(cls, officeCode):
        MySql.openConnection()
        MySql.query(f"select * from offices where officeCode = {officeCode}")
        results = MySql.getResults()
        office = Office(results[0][0], results[0][1], results[0][2], results[0][3], results[0][4], results[0][5], results[0][6], results[0][7], results[0][8],)
        MySql.closeConnection()
        return office

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
