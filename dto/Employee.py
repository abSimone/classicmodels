class Employee:
    def __init__(self, employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle):
        self.employeeNumber = employeeNumber
        self.lastName = lastName
        self.firstName = firstName
        self.extension = extension
        self.email = email
        self.officeCode = officeCode
        self.reportsTo = reportsTo
        self.jobTitle = jobTitle

    # getter

    @property
    def employeeNumber(self):
        return self._employeeNumber

    @property
    def lastName(self):
        return self._lastName

    @property
    def firstName(self):
        return self._firstName

    @property
    def extension(self):
        return self._extension

    @property
    def email(self):
        return self._email

    @property
    def officeCode(self):
        return self._officeCode

    @property
    def reportsTo(self):
        return self._reportsTo

    @property
    def jobTitle(self):
        return self._jobTitle

    # setter

    @employeeNumber.setter
    def employeeNumber(self, employeeNumber):
        self._employeeNumber = employeeNumber

    @lastName.setter
    def lastName(self, lastName):
        self._lastName = lastName

    @firstName.setter
    def firstName(self, firstName):
        self._firstName = firstName

    @extension.setter
    def extension(self, extension):
        self._extension = extension

    @email.setter
    def email(self, email):
        self._email = email

    @officeCode.setter
    def officeCode(self, officeCode):
        self._officeCode = officeCode

    @reportsTo.setter
    def reportsTo(self, reportsTo):
        self._reportsTo = reportsTo

    @jobTitle.setter
    def jobTitle(self, jobTitle):
        self._jobTitle = jobTitle

    def __str__(self):
        return f"numero impiegato: {self._employeeNumber}, cognome: {self._lastName}, nome: {self._firstName}, estensione: {self._extension}, email {self._email}, codice ufficio: {self._officeCode}, riferisce a: {self._reportsTo}, titolo: {self._jobTitle}"
