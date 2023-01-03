class Employeedto:
    def __init__(self, employee_number, last_name, first_name, extension, email, office_code, reportsto, jobtitle):
        self.employee_number=employee_number
        self.last_name=last_name
        self.first_name=first_name
        self.extension=extension
        self.email=email
        self.office_code=office_code
        self.reportsto=reportsto
        self.jobtitle=jobtitle

    def __str__(self):
        return f'{self._employee_number} , {self._last_name},{self._first_name},{self._extension},{self._email},{self._office_code},{self._reportsto}{self._jobtitle}'


    @property
    def employee_number(self):
        return self._employee_number

    @employee_number.setter
    def employee_number(self, employee_number):
        self._employee_number = employee_number

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

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
    def office_code(self):
        return self._office_code

    @office_code.setter
    def office_code(self, office_code):
        self._office_code = office_code
    
    @property
    def reportsto(self):
        return self._reportsto

    @reportsto.setter
    def reportsto(self, reportsto):
        self._reportsto = reportsto

    @property
    def _jobtitle(self):
        return self.__jobtitle

    @_jobtitle.setter
    def _jobtitle(self, _jobtitle):
        self.__jobtitle = _jobtitle    