class Customer:
    def __init__(self, customernumber, name,lastname,firstname,phone,addressLine1):
        self.customerNumber=customernumber
        self.customerName=name
        self.contactLastName=lastname
        self.contactFirstName=firstname
        self.phone=phone
        self.addressLine1=addressLine1
        
    @property
    def customerNumber(self):
        return self._customerNumber 
    
    @customerNumber.setter    
    def customerNumber(self, customerNumber):
        self._customerNumber = customerNumber
        
    @property
    def customerName(self):
        return self._customerName
    
    @customerName.setter    
    def customerNumber(self, customerName):
        self._customerName = customerName
    
    @property
    def contactLastName(self):
        return self._contactLastName 
    
    @contactLastName.setter    
    def contactLastName(self, contactLastName):
        self._contactLastName = contactLastName
        
    @property
    def contactFirstName(self):
        return self._contactFirstName 
    
    @contactFirstName.setter    
    def contactFirstName(self, contactFirstName):
        self._contactFirstName = contactFirstName
        
    @property
    def phone(self):
        return self._phone 
    
    @phone.setter    
    def phone(self, phone):
        self._phone = phone
        
    @property
    def addressLine1(self):
        return self._addressLine1 
    
    @addressLine1.setter    
    def addressLine1(self, addressLine1):
        self._addressLine1 = addressLine1
        
        
        
 
