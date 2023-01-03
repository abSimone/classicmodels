class Products:
    def __init__(self, productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP):
        self.productCode = productCode
        self.productName = productName
        self.productLine = productLine
        self.productScale = productScale
        self.productVendor = productVendor
        self.productDescription = productDescription
        self.quantityInStock = quantityInStock
        self.buyPrice = buyPrice
        self.MSRP = MSRP
        self.firstInit = True
        
    def __init__(self, productCode):
        self.productCode = productCode
        self.firstInit = False


    # getter
    @property
    def productCode(self):
        return self._productCode

    @property
    def productName(self):
        return self._productName

    @property
    def productLine(self):
        return self._productLine

    @property
    def productScale(self):
        return self._productScale

    @property
    def productVendor(self):
        return self._productVendor

    @property
    def productDescription(self):
        return self._productDescription

    @property
    def quantityInStock(self):
        return self._quantityInStock

    @property
    def buyPrice(self):
        return self._buyPrice

    @property
    def MSRP(self):
        return self._MSRP

    # setter

    @productCode.setter
    def productCode(self, productCode):
        self._productCode = productCode

    @productName.setter
    def productName(self, productName):
        self._productName = productName

    @productLine.setter
    def productLine(self, productLine):
        self._productLine = productLine

    @productScale.setter
    def productScale(self, productScale):
        self._productScale = productScale

    @productVendor.setter
    def productVendor(self, productVendor):
        self._productVendor = productVendor

    @productDescription.setter
    def productDescription(self, productDescription):
        self._productDescription = productDescription

    @quantityInStock.setter
    def quantityInStock(self, quantityInStock):
        self._quantityInStock = quantityInStock

    @buyPrice.setter
    def buyPrice(self, buyPrice):
        self._buyPrice = buyPrice

    @MSRP.setter
    def MSRP(self, MSRP):
        self._MSRP = MSRP

    def __str__(self):
        if self.firstInit == True:
            return f"codice prodotto: {self._productCode}, nome prodotto: {self._productName}, linea prodotto: {self._productLine}, scala prodotto: {self._productScale}, venditore: {self._productVendor}, descrizione: {self._productDescription}, scorte: {self._quantityInStock}, prezzo d'acquisto: {self._buyPrice}, MSRP : {self._MSRP}"
        else:
            return f"codice prodotto: {self._productCode}"
