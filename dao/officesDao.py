from dao.utility.db import MySql
from dto.Office import Office


class OfficeDao:
    # read
    @classmethod
    def getAllOffices(cls):
        MySql.openConnection()
        MySql.query("select * from offices")
        results = MySql.getResults()
        offices = []
        for office in results:
           offices.append(Office(office[0], office[1], office[2], office[3], office[4], office[5], office[6], office[7], office[8],)) 
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
