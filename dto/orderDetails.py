class Office:
    def __init__(self, orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber):
        self._orderNumber=orderNumber
        self._productCode=productCode
        self._quantityOrdered=quantityOrdered
        self._priceEach=priceEach
        self._orderLineNumber=orderLineNumber
  
    @property
    def orderNumber(self):
        return self._orderNumber 
    
    @orderNumber.setter    
    def orderNumber(self, orderNumber):
        self._orderNumber = orderNumber
        
    @property
    def productCode(self):
        return self.productCode
    
    @productCode.setter    
    def productCode(self, productCode):
        self._productCode = productCode
    
    @property
    def quantityOrdered(self):
        return self._quantityOrdered
    
    @quantityOrdered.setter    
    def quantityOrdered(self, quantityOrdered):
        self._quantityOrdered = quantityOrdered
        
    @property
    def priceEach(self):
        return self._priceEach 
    
    @priceEach.setter    
    def priceEach(self, priceEach):
        self._priceEach = priceEach
        
    @property
    def orderLineNumber(self):
        return self._orderLineNumber 
    
    @orderLineNumber.setter    
    def orderLineNumber(self, orderLineNumber):
        self._orderLineNumber = orderLineNumber
    
    def __str__(self):
        return f"Numero ordine: {self._orderNumber}, Codice prodotto: {self._productCode}, Quantità ordini: {self._quantityOrdered}, Prezzo cadauno: {self._priceEach}, Numero linea ordine: {self._orderLineNumber}"