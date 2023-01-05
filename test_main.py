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

    assert response.json() == {"customerNumber": "0001"}


def test_get_customer():
    response = client.get('/customer/all'
                          )
    assert response.status_code == 200
    assert len(response.json()) > 0


# offices
def test_new_office():
    response = client.post('/offices/new',
                           json={
                               "officeCode": "5",
                               "city": "philadephia",
                               "phone": "355688597",
                               "addressLine1": "via veneto 36",
                               "addressLine2": "scala b int 8",
                               "state": "italia",
                               "country": "italia",
                               "postalCode": "00000",
                               "territory": "random",
                           }
                           )
    assert response.status_code == 201
    assert response.json() == {"officeCode": "5"}


def test_get_office():
    response = client.get('/offices/all'
                          )
    assert response.status_code == 200
    assert len(response.json()) > 0


# orders
def test_new_order():
    response = client.post('/orders/new',
                           json={
                               "orderNumber": 500,
                               "orderDate": 2023-1-23,
                               "requiredDate": 2023-1-26,
                               "shippedDate": 2023-1-27,
                               "status": "processing",
                               "comments": "",
                               "customerNumber": 13,
                           }
                           )
    assert response.status_code == 201
    assert response.json() == {"orderNumber": 500}


def test_get_orders():
    response = client.get('/orders/all'
                          )
    assert response.status_code == 200
    assert len(response.json()) > 0


# orders_detail
def test_new_order_details():
    response = client.post('/order_details/new',
                           json={
                               "orderNumber": 510,
                               "productCode": "1321",
                               "quantityOrdered": 24,
                               "priceEach": 10.5,
                               "orderLineNumber": 123,
                           }
                           )
    assert response.status_code == 201
    assert response.json() == {"productCode": "1321"}


def test_get_order_details():
    response = client.get('/order_details/all'
                          )
    assert response.status_code == 200
    assert len(response.json()) > 0
    
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
