from pydantic import BaseModel

class CustomerModel (BaseModel):
  customerName : str
  customerNumber : str
  contactLastName : str
  contactFirstName : str
  phone : str
  addressLine1 : str
  addressLine2 : str
  city : str
  state : str
  postalCode : str
  country : str
  salesRepEmployeeNumber : str
  creditLimit : str

