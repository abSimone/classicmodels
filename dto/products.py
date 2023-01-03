class Products:
    def __init__(self, pCode, pName,pLine,pScale,pVendor,pDescription,qntStock,buyPrice,Msrp):
        self._productCode=pCode
        self._productName=pName
        self._productLine=pLine
        self._productScale=pScale
        self._productVendor=pVendor
        self._productDescription=pDescription
        self._quantityInStock=qntStock
        self._buyPrice=buyPrice
        self._MSRP=Msrp
        
    @property
    def productCode(self):
        return self._productCode 
    
    @productCode.setter    
    def productCode(self, productCode):
        self._productCode = productCode
        
    @property
    def productName(self):
        return self._productName
    
    @productName.setter    
    def productName(self, productName):
        self._productName = productName
    
    @property
    def productLine(self):
        return self._productLine 
    
    @productLine.setter    
    def productLine(self, productLine):
        self._productLine = productLine
        
    @property
    def productScale(self):
        return self._productScale 
    
    @productScale.setter    
    def productScale(self, productScale):
        self._productScale = productScale
        
    @property
    def productVendor(self):
        return self._productVendor 
    
    @productVendor.setter    
    def productVendor(self, productVendor):
        self._productVendor = productVendor
        
    @property
    def productDescription(self):
        return self._productDescription 
    
    @productDescription.setter    
    def productDescription(self, productDescription):
        self._productDescription = productDescription
    
    @property
    def quantityInStock(self):
        return self._quantityInStock 
    
    @quantityInStock.setter    
    def quantityInStock(self, quantityInStock):
        self._quantityInStock = quantityInStock
    
    @property
    def buyPrice(self):
        return self._buyPrice 
    
    @buyPrice.setter    
    def buyPrice(self, buyPrice):
        self._buyPrice = buyPrice
    
    @property
    def MSRP(self):
        return self._MSRP 
    
    @MSRP.setter    
    def MSRP(self, MSRP):
        self._MSRP = MSRP
        
    def __str__(self):
        return f"codice: {self._productCode}, nome: {self._productName}, linea: {self._productLine}, ScalaProdotto: {self._productScale}, Venditore: {self._productVendor}, Descrizione: {self._productDescription}, quantita: {self._quantityInStock}, prezzo di acquisto: {self._buyPrice}, MSRP: {self._MSRP}"
        