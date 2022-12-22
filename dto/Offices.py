class Offices:
    def __init__(self, officeCode, city, phone, addressLine1, addressLine2, state, country, postalCode, territory):
        self.officeCode=officeCode
        self.city=city 
        self.phone=phone
        self.addressLine1=addressLine1 
        self.addressLine2=addressLine2 
        self.state=state 
        self.country=country 
        self.postalCode=postalCode 
        self.territory=territory
        
    @property
    def officeCode(self):
        return self.officeCode
    
    @officeCode.setter
    def officeCode(self, new_office_code):
        self.officeCode=new_office_code
        
    @property
    def city(self):
        return self.city
    
    @city.setter
    def city(self, new_city):
        self.city=new_city
        
    @property
    def phone(self):
        return self.phone
    
    @phone.setter
    def phone(self, new_phone):
        self.phone=new_phone
        
    @property
    def addressLine1(self):
        return self.addressLine1
    
    @addressLine1.setter
    def addressLine1(self, new_address_line_1):
        self.addressLine1=new_address_line_1
        
    @property
    def addressLine2(self):
        return self.addressLine2
    
    @addressLine2.setter
    def addressLine2(self, new_address_line_2):
        self.addressLine2=new_address_line_2
        
    @property
    def state(self):
        return self.state
    
    @state.setter
    def state(self, new_state):
        self.state=new_state
        
    @property
    def country(self):
        return self.country
    
    @country.setter
    def country(self, new_country):
        self.country=new_country
        
    @property
    def postalCode(self):
        return self.postalCode
    
    @postalCode.setter
    def postalCode(self, new_postal_code):
        self.postalCode=new_postal_code
        
    @property
    def territory(self):
        return self.territory
    
    @territory.setter
    def territory(self, new_territory):
        self.territory=new_territory