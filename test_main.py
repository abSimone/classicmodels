from .main import app
from fastapi.testclient import TestClient
from models.payment import Payment_model

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
    
def test_all_payments():
    response = client.get('/payments/all')
    assert response.status_code == 200
    assert len(response.json()) > 0
    
def test_new_payment():
    response = client.post('/payments/new',
                           json = {
                               "customer_number": 50,
                                "check_number": "string",
                                "payment_date": "string",
                                "amount": 0
                           })
    assert response.status_code == 201
    assert response.json() == {'check_number': 'string'}
    
def test_all_products():
    response = client.get('/products/all')
    assert response.status_code == 200
    assert len(response.json()) > 0
    
def test_new_product():
    response = client.post('/products/new',
                           json = {
                               "productCode": "string",
                                "productLine": "string",
                                "productScale": "string",
                                "productName": "string",
                                "productVendor": "string",
                                "productDescription": "string",
                                "quantityInStock": "string",
                                "buyPrice": "string",
                                "MSRP": "string",
                                "firstInit": 'True'
                           })
    assert response.status_code == 201
    assert response.json() == {'productCode': 'string'}
