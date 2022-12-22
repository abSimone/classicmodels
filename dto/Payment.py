class Payment:
    def __init__(self, customerNumber, checkNumber, paymentDate, amount):
        self.customerNumber = customerNumber
        self.checkNumber = checkNumber
        self.paymentDate = paymentDate
        self.amount = amount

    # getter
    @property
    def customerNumber(self):
        return self._customerNumber

    @property
    def checkNumber(self):
        return self._checkNumber

    @property
    def paymentDate(self):
        return self._paymentDate

    @property
    def amount(self):
        return self._amount

    # setter

    @customerNumber.setter
    def customerNumber(self, customerNumber):
        self._customerNumber = customerNumber

    @checkNumber.setter
    def checkNumber(self, checkNumber):
        self._checkNumber = checkNumber

    @paymentDate.setter
    def paymentDate(self, paymentDate):
        self._paymentDate = paymentDate

    @amount.setter
    def amount(self, amount):
        self._amount = amount
        
    def __str__(self):
        return f"numero cliente: {self._customerNumber}, numero check: {self._checkNumber}, data pagamento: {self._paymentDate}, totale: {self._amount}"
