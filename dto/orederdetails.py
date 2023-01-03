class Orderdetailsdto:
    def __init__(self, order_number, product_code, quantity_orderd, price_each, ordeline_number, office_code, reportsto, jobtitle):
        self.order_number=order_number
        self.product_code=product_code
        self.quantity_orderd=quantity_orderd
        self.price_each=price_each
        self.ordeline_number=ordeline_number
        

    def __str__(self):
        return f'{self._order_number} , {self._product_code},{self._quantity_orderd},{self._price_each},{self._ordeline_number},'


    @property
    def order_number(self):
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        self._order_number = order_number

    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, product_code):
        self._product_code = product_code

    @property
    def quantity_orderd(self):
        return self._quantity_orderd

    @quantity_orderd.setter
    def quantity_orderd(self, quantity_orderd):
        self._quantity_orderd = quantity_orderd

    @property
    def price_each(self):
        return self._price_each

    @price_each.setter
    def price_each(self, price_each):
        self._price_each = price_each

    @property
    def ordeline_number(self):
        return self._ordeline_number
    @ordeline_number.setter

    def ordeline_number(self, ordeline_number):
        self._ordeline_number = ordeline_number