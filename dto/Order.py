class Order:
    def __init__(self, ordernumber, date,reqdate,shipdate,status,comments,customernumber):
        self.orderNumber=ordernumber
        self.requiredDate=date
        self.shippedDate=shipdate
        self.status=status
        self.comments=comments
        self.customerNumber=customernumber
        
    @property
    def orderNumber(self):
        return self.orderNumber 
    
    @orderNumber.setter    
    def orderNumber(self, orderNumber):
        self.orderNumber = orderNumber
        
    @property
    def requiredDate(self):
        return self.requiredDate
    
    @requiredDate.setter    
    def requiredDate(self, requiredDate):
        self.requiredDate = requiredDate
    
    @property
    def shippedDate(self):
        return self.shippedDate 
    
    @shippedDate.setter    
    def shippedDate(self, shippedDate):
        self.shippedDate = shippedDate
        
    @property
    def status(self):
        return self.status 
    
    @status.setter    
    def status(self, status):
        self.status = status
        
    @property
    def comments(self):
        return self.comments 
    
    @comments.setter    
    def comments(self, comments):
        self.comments = comments
        
    @property
    def customerNumber(self):
        return self.customerNumber 
    
    @customerNumber.setter    
    def customerNumber(self, customerNumber):
        self.customerNumber = customerNumber
        
        
        
 