class Customer:
    # def __init__(self,lastname, firstname):
    #     self._contactLastName=lastname
    #     self._contactFirstName=firstname      
    #     self._firstinit = True
        
    def __init__(self, **kwargs):
        if kwargs.get('customerNumber') != None:
            self.customerNumber = kwargs.get('customerNumber')
        if kwargs.get('customerName') != None:
            self.customerName = kwargs.get('customerName')
        if kwargs.get('contactLastName') != None:
            self.contactLastName = kwargs.get('contactLastName')
        if kwargs.get('contactFirstName') != None:
            self.contactFirstName = kwargs.get('contactFirstName')
        if kwargs.get('phone') != None:
            self.phone = kwargs.get('phone')
        if kwargs.get('addressLine1') != None:
            self.addressLine1 = kwargs.get('addressLine1')
        if kwargs.get('addressLine2') != None:
            self.addressLine2 = kwargs.get('addressLine2')
        if kwargs.get('city') != None:
            self.city = kwargs.get('city')
        if kwargs.get('state') != None:
            self.state = kwargs.get('state')
        if kwargs.get('postalCode') != None:
            self.postalCode = kwargs.get('postalCode')
        if kwargs.get('country') != None:
            self.country = kwargs.get('country')
        if kwargs.get('salesRepEmployeeNumber') != None:
            self.salesRepEmployeeNumber = kwargs.get('salesRepEmployeeNumber')
        if kwargs.get('creditLimit') != None:
            self.creditLimit = kwargs.get('creditLimit')
        
        self.string = ''
        for key in kwargs:
            self.string += f'{key} = {kwargs[key]}, '
        
      
    # def __init__(self, customernumber, name, lastname, firstname, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit):
    #     self._customerNumber=customernumber
    #     self._customerName=name
    #     self._contactLastName=lastname
    #     self._contactFirstName=firstname
    #     self._phone=phone
    #     self._addressLine1=addressLine1
    #     self._addressLine2=addressLine2
    #     self._city=city
    #     self._state=state
    #     self._postalCode=postalCode
    #     self._country=country
    #     self._salesRepEmployeeNumber=salesRepEmployeeNumber
    #     self._creditLimit=creditLimit
    #     self._firstinit = False
        
        
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
    def customerName(self, customerName):
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
        
    @property
    def addressLine2(self):
        return self._addressLine2
    
    @addressLine2.setter    
    def addressLine2(self, addressLine2):
        self._addressLine2 = addressLine2
        
    @property
    def city(self):
        return self._city
    
    @city.setter    
    def city(self, city):
        self._city = city
        
    @property
    def state(self):
        return self._state
    
    @state.setter    
    def state(self, state):
        self._state = state
        
    @property
    def postalCode(self):
        return self._postalCode
    
    @postalCode.setter    
    def postalCode(self, postalCode):
        self._postalCode = postalCode
        
    @property
    def country(self):
        return self._country
    
    @country.setter    
    def country(self, country):
        self._country = country
        
    @property
    def salesRepEmployeeNumber(self):
        return self._salesRepEmployeeNumber 
    
    @salesRepEmployeeNumber.setter    
    def salesRepEmployeeNumber(self, salesRepEmployeeNumber):
        self._salesRepEmployeeNumber = salesRepEmployeeNumber
        
    @property
    def creditLimit(self):
        return self._creditLimit
    
    @creditLimit.setter    
    def creditLimit(self, creditLimit):
        self._creditLimit = creditLimit
    
    # def __str__(self):
    #     return f'cognome contatto: {self._contactLastName}, nome contatto: {self._contactFirstName}'
    def __str__(self):
        # return f"Numero cliente: {self._customerNumber}, nome cliente: {self._customerName}, cognome contatto: {self._contactLastName}, nome contatto: {self._contactFirstName}, telefono {self._phone}, indirizzo 1: {self._addressLine1}, indirizzo 2: {self._addressLine2}, città: {self._city}, stato: {self._state}, codice postale: {self._postalCode}, paese: {self._country}, salesRepEmployeeNumber: {self._salesRepEmployeeNumber}, limite dredito:{self._creditLimit}"
        return self.string
            # return f'cognome contatto: {self._contactLastName}, nome contatto: {self._contactFirstName}'
        
 