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
        return self.customerNumber 
    
    @customerNumber.setter    
    def customerNumber(self, customerNumber):
        self.customerNumber = customerNumber
        
    @property
    def customerName(self):
        return self.customerName
    
    @customerName.setter    
    def customerNumber(self, customerName):
        self.customerName = customerName
    
    @property
    def contactLastName(self):
        return self.contactLastName 
    
    @contactLastName.setter    
    def contactLastName(self, contactLastName):
        self.contactLastName = contactLastName
        
    @property
    def contactFirstName(self):
        return self.contactFirstName 
    
    @contactFirstName.setter    
    def contactFirstName(self, contactFirstName):
        self.contactFirstName = contactFirstName
        
    @property
    def phone(self):
        return self.phone 
    
    @phone.setter    
    def phone(self, phone):
        self.phone = phone
        
    @property
    def addressLine1(self):
        return self.addressLine1 
    
    @addressLine1.setter    
    def addressLine1(self, addressLine1):
        self.addressLine1 = addressLine1
        
        
        
 