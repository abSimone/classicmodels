class Orders:
    def __init__(self, orderNumber, orderDate, requiredDate, shippedDate, status, comments, customerNumber):
        self.orderNumber=orderNumber
        self.orderDate=orderDate
        self.requiredDate=requiredDate
        self.shippedDate=shippedDate
        self.status=status
        self.comments=comments
        self.customerNumber=customerNumber

    def __str__(self):
        return f'{self._orderNumber} , {self._orderDate},{self._requiredDate},{self._shippedDate},{self._status},{self._comments},{self._customerNumber}'


    @property
    def orderNumber(self):
        return self._orderNumber

    @orderNumber.setter
    def orderNumber(self, orderNumber):
        self._orderNumber = orderNumber

    @property
    def orderDate(self):
        return self._orderDate

    @orderDate.setter
    def orderDate(self, orderDate):
        self._orderDate = orderDate

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