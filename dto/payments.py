class Payments:
    def __init__(self, customerNumber, checkNumber, paydate , amount):
        self._customerNumber=customerNumber
        self._checkNumber=checkNumber
        self._paymentDate=paydate
        self._amount=amount
    
    @property
    def customerNumber(self):
        return self._customerNumber 
    
    @customerNumber.setter    
    def customerNumber(self, costomerNumber):
        self._customerNumber = costomerNumber
        
    @property
    def checkNumber(self):
        return self._checkNumber
    
    @checkNumber.setter    
    def checkNumber(self, checkNumber):
        self._checkNumber = checkNumber
    
    @property
    def paymentDate(self):
        return self._paymentDate 
    
    @paymentDate.setter    
    def paymentDate(self, paymentDate):
        self._paymentDate = paymentDate
        
    @property
    def amount(self):
        return self._amount 
    
    @amount.setter    
    def amount(self, amount):
        self._amount = amount
        
    def __str__(self):
        return f"cnumber: {self._customerNumber}, checknumber: {self._checkNumber}, datapagamento: {self._paymentDate}, ammontare: {self._amount}"