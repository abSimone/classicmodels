class Office:
    def __init__(self, officeCode, city, phone, addressLine1, addressLine2, state, country, postalCode, territory):
        self._officeCode=officeCode
        self._city=city
        self._phone=phone
        self._addressLine1=addressLine1
        self._addressLine2=addressLine2
        self._state=state
        self._country = country
        self._postalCode = postalCode
        self._territory = territory
  
    @property
    def officeCode(self):
        return self._officeCode 
    
    @officeCode.setter    
    def officeCode(self, officeCode):
        self._officeCode = officeCode
        
    @property
    def city(self):
        return self._city
    
    @city.setter    
    def city(self, city):
        self._city = city
    
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
    def state(self):
        return self._state 
    
    @state.setter    
    def state(self, state):
        self._state = state
        
    @property
    def country(self):
        return self._country 
    
    @country.setter    
    def country(self, country):
        self._country = country
        
    @property
    def postalCode(self):
        return self._postalCode 
    
    @state.setter    
    def postalCode(self, postalCode):
        self._postalCode = postalCode
        
    @property
    def territory(self):
        return self._territory 
    
    @territory.setter    
    def territory(self, territory):
        self._territory = territory
    
    def __str__(self):
        return f"codice: {self._officeCode}, città: {self._city}, telefono: {self._phone}, indirizzo 1: {self._addressLine1}, indirizzo 2 {self._addressLine2}, stato: {self._state}, regione: {self._country}, codice postale: {self._postalCode}, territorio: {self._territory}"