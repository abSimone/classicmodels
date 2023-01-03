class Order:
    def __init__(self, orderNumber, orderDate, requiredDate, shippedDate, status, comments, customerNumber):
        self.orderNumber = orderNumber
        self.orderDate = orderDate
        self.requiredDate = requiredDate
        self.shippedDate = shippedDate
        self.status = status
        self.comments = comments
        self.customerNumber = customerNumber
        self.firstInit = True
        
    def __init__(self, orderNumber):
        self.orderNumber = orderNumber
        self.firstInit = False

    # getter
    @property
    def orderNumber(self):
        return self._orderNumber

    @property
    def orderDate(self):
        return self._orderDate

    @property
    def requiredDate(self):
        return self._requiredDate

    @property
    def shippedDate(self):
        return self._shippedDate

    @property
    def status(self):
        return self._status

    @property
    def comments(self):
        return self._comments

    @property
    def customerNumber(self):
        return self._customerNumber


    # setter

    @orderNumber.setter
    def orderNumber(self, orderNumber):
        self._orderNumber = orderNumber

    @orderDate.setter
    def orderDate(self, orderDate):
        self._orderDate = orderDate

    @requiredDate.setter
    def requiredDate(self, requiredDate):
        self._requiredDate = requiredDate

    @shippedDate.setter
    def shippedDate(self, shippedDate):
        self._shippedDate = shippedDate

    @status.setter
    def status(self, status):
        self._status = status

    @comments.setter
    def comments(self, comments):
        self._comments = comments

    @customerNumber.setter
    def customerNumber(self, customerNumber):
        self._customerNumber = customerNumber


    def __str__(self):
        if self.firstInit == True:
            return f"Numero ordine: {self._orderNumber}, data ordine: {self._orderDate}, data richiesta: {self._requiredDate}, data consegna: {self._shippedDate}, status {self._status}, commenti: {self._comments}, numero cliente: {self._customerNumber}"
        else:
            return f"Numero ordine: {self._orderNumber}"
