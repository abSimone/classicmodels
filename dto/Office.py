class Office:
    def __init__(self, officeCode, city, phone, addressLine1, addressLine2, state, country, postalCode, territory):
        self.officeCode=officeCode
        self.city=city
        self.phone=phone
        self.addressLine1=addressLine1
        self.addressLine2=addressLine2
        self.state=state
        self.country = country
        self.postalCode = postalCode
        self.territory = territory
  
    @property
    def officeCode(self):
        return self.officeCode 
    
    @officeCode.setter    
    def officeCode(self, officeCode):
        self.officeCode = officeCode
        
    @property
    def city(self):
        return self.city
    
    @city.setter    
    def city(self, city):
        self.city = city
    
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
        
    @property
    def addressLine2(self):
        return self.addressLine2 
    
    @addressLine2.setter    
    def addressLine2(self, addressLine2):
        self.addressLine2 = addressLine2
        
    @property
    def state(self):
        return self.state 
    
    @state.setter    
    def state(self, state):
        self.state = state
        
    @property
    def country(self):
        return self.country 
    
    @country.setter    
    def country(self, country):
        self.country = country
        
    @property
    def postalCode(self):
        return self.postalCode 
    
    @state.setter    
    def postalCode(self, postalCode):
        self.postalCode = postalCode
        
    @property
    def territory(self):
        return self.territory 
    
    @territory.setter    
    def territory(self, territory):
        self.territory = territory