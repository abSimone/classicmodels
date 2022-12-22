
from dto.Order import Order
from dto.Product import Products

class OrderDetails:
    def __init__(self, orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber):
        self.orderNumber = Order(orderNumber)
        self.productCode = Products(productCode)
        self.quantityOrdered = quantityOrdered
        self.priceEach = priceEach
        self.orderLineNumber = orderLineNumber

    # getter
    @property
    def orderNumber(self):
        return self._orderNumber

    @property
    def productCode(self):
        return self._productCode

    @property
    def quantityOrdered(self):
        return self._quantityOrdered

    @property
    def priceEach(self):
        return self._priceEach

    @property
    def orderLineNumber(self):
        return self._orderLineNumber

    # setter

    @orderNumber.setter
    def orderNumber(self, orderNumber):
        self._orderNumber = orderNumber

    @productCode.setter
    def productCode(self, productCode):
        self._productCode = productCode

    @quantityOrdered.setter
    def quantityOrdered(self, quantityOrdered):
        self._quantityOrdered = quantityOrdered

    @priceEach.setter
    def priceEach(self, priceEach):
        self._priceEach = priceEach

    @orderLineNumber.setter
    def orderLineNumber(self, orderLineNumber):
        self._orderLineNumber = orderLineNumber

    def __str__(self):
        return f"{self._orderNumber}, {self._productCode}, quantità ordinata: {self._quantityOrdered}, prezzo individuale: {self._priceEach}\u20ac, numero linea ordine {self._orderLineNumber}"
