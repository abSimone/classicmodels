from .main import app
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
