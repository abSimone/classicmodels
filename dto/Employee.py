class Employee:
    def __init__(self, employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle):

        self._employeeNumber = employeeNumber
        self._lastName=lastName
        self._firstName=firstName
        self._extension=extension
        self._email=email
        self._officeCode=officeCode
        self._reportsTo = reportsTo
        self._jobTitle = jobTitle
  
    @property
    def employeeNumber(self):
        return self._employeeNumber 
    
    @employeeNumber.setter    
    def employeeNumber(self, employeeNumber):
        self._employeeNumber = employeeNumber
        
    @property
    def lastName(self):
        return self._lastName
    
    @lastName.setter    
    def lastName(self, lastName):
        self._lastName = lastName
    
    @property
    def firstName(self):
        return self._firstName 
    
    @firstName.setter    
    def firstName(self, firstName):
        self._firstName = firstName
        
    @property
    def extension(self):
        return self._extension 
    
    @extension.setter    
    def extension(self, extension):
        self._extension = extension
        
    @property
    def email(self):
        return self._email 
    
    @email.setter    
    def email(self, email):
        self._email = email
        
    @property
    def officeCode(self):
        return self._officeCode 
    
    @officeCode.setter    
    def officeCode(self, officeCode):
        self._officeCode = officeCode
        
    @property
    def reportsTo(self):
        return self._reportsTo 
    
    @reportsTo.setter    
    def reportsTo(self, reportsTo):
        self._reportsTo = reportsTo
        
    @property
    def jobTitle(self):
        return self._jobTitle 
    
    @jobTitle.setter    
    def jobTitle(self, jobTitle):
        self._jobTitle = jobTitle
        
    
    def __str__(self):
        return f"Numero dipendente: {self._employeeNumber}, cognome: {self._lastName}, nome: {self._firstName}, estensione: {self._extension}, email: {self._email}, riferimento: {self._reportsTo}, titolo lavoro: {self._jobTitle}"
