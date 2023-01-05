from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_new_customer():
    response = client.post('/customer/new',
                           json={
                               "customerName": "customer1",
                               "customerNumber": "0001",
                               "contactLastName": "Rossi",
                               "contactFirstName": "Mario",
                               "phone": "355685548",
                               "addressLine1": "via veneto 36",
                               "addressLine2": "scala b int 8",
                               "city": "roma",
                               "state": "italia",
                               "postalCode": "00000",
                               "country": "italia",
                               "salesRepEmployeeNumber": "00002",
                               "creditLimit": "9000.23"
                           }
                           )
    assert response.status_code == 201
    assert response.json() == {"customerNumber" : "0001"}

def test_getEmployee():
    response = client.get('/employee/all')
    assert response.status_code==200
    assert len(response.json())>0

def test_new_employee():
    response = client.post('/employee/new',
                           json={
                               "employeeNumber": "e0",
                                "lastName": "a",
                                "firstName": "b",
                                "extension": "c",
                                "email": "d",
                                "officeCode": "d",
                                "reportsTo": "e",
                                "jobTitle": "f"
                           }
                           )
    assert response.status_code==200

def test_getProductLine():
    response = client.get('/productLines/all')
    assert response.status_code==200
    assert len(response.json())>0

def test_new_productline():
    response = client.post('/productLines/new',
                           json={
                               "productLine": "pl1",
                                "textDescription": "a",
                                "htmlDescription": " ",
                                "image": " "
                           }
                           )
    assert response.status_code==200