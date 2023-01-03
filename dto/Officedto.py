class Officedto:
    def __init__(self, officeCode, city, phone, addressLine1, addressLine2, state, country, postalCode, territory):
        self.officeCode = officeCode
        self.city = city
        self.phone = phone
        self.addressLine1 = addressLine1
        self.addressLine2 = addressLine2
        self.state = state
        self.country = country
        self.postalCode = postalCode
        self.territory = territory

    # getter
    @property
    def officeCode(self):
        return self._officeCode

    @property
    def city(self):
        return self._city

    @property
    def phone(self):
        return self._phone

    @property
    def addressLine1(self):
        return self._addressLine1

    @property
    def addressLine2(self):
        return self._addressLine2

    @property
    def state(self):
        return self._state

    @property
    def country(self):
        return self._country

    @property
    def postalCode(self):
        return self._postalCode

    @property
    def territory(self):
        return self._territory


    @officeCode.setter
    def officeCode(self, officeCode):
        self._officeCode = officeCode

    @city.setter
    def city(self, city):
        self._city = city

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @addressLine1.setter
    def addressLine1(self, addressLine1):
        self._addressLine1 = addressLine1

    @addressLine2.setter
    def addressLine2(self, addressLine2):
        self._addressLine2 = addressLine2

    @state.setter
    def state(self, state):
        self._state = state

    @country.setter
    def country(self, country):
        self._country = country

    @postalCode.setter
    def postalCode(self, postalCode):
        self._postalCode = postalCode

    @territory.setter
    def territory(self, territory):
        self._territory = territory
        
    def __str__(self):
        return f"codice: {self._officeCode}, città: {self._city}, telefono: {self._phone}, indirizzo 1: {self._addressLine1}, indirizzo 2 {self._addressLine2}, stato: {self._state}, regione: {self._country}, codice postale: {self._postalCode}, territorio: {self._territory}"
