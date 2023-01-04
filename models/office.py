from pydantic import BaseModel

class OfficeModel (BaseModel):
  officeCode : str
  city : str
  phone : str | None = None
  addressLine1 : str
  addressLine2 : str
  state : str
  country : str
  postalCode : str
  territory : str

