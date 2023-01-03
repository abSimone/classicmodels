class Order:
    def __init__(self, orderNumber, orderDate, requiredDate, shippedDate, status, comments, customerNumber):
        self._orderNumber=orderNumber
        self._orderDate = orderDate
        self._requiredDate=requiredDate
        self._shippedDate=shippedDate
        self._status=status
        self._comments=comments
        self._customerNumber=customerNumber
        
    @property
    def orderNumber(self):
        return self._orderNumber 
    
    @orderNumber.setter    
    def orderNumber(self, orderNumber):
        self._orderNumber = orderNumber
        
    @property
    def requiredDate(self):
        return self._requiredDate
    
    @requiredDate.setter    
    def requiredDate(self, requiredDate):
        self._requiredDate = requiredDate
    
    @property
    def shippedDate(self):
        return self._shippedDate 
    
    @shippedDate.setter    
    def shippedDate(self, shippedDate):
        self._shippedDate = shippedDate
        
    @property
    def status(self):
        return self._status 
    
    @status.setter    
    def status(self, status):
        self._status = status
        
    @property
    def comments(self):
        return self._comments 
    
    @comments.setter    
    def comments(self, comments):
        self._comments = comments
        
    @property
    def customerNumber(self):
        return self._customerNumber 
    
    @customerNumber.setter    
    def customerNumber(self, customerNumber):
        self._customerNumber = customerNumber
        
    def __str__(self):
        return f"Numero ordine: {self._orderNumber}, data ordine: {self._orderDate}, data richiesta: {self._requiredDate}, data di spedizione: {self._shippedDate}, stato: {self._status}, commenti: {self._comments}, numero cliente: {self._customerNumber}"
