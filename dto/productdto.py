class Productdto:
    def __init__(self, product_code, product_name, product_line, product_scale, product_vendor, product_description, quantity_instock, buyprice, msrp):
        self.product_code=product_code
        self.product_name=product_name
        self.product_line=product_line
        self.product_scale=product_scale
        self.product_vendor=product_vendor
        self.product_description=product_description
        self.quantity_instock=quantity_instock
        self.buyprice=buyprice
        self.msrp=msrp

    def __str__(self):
        return f'{self._product_code} , {self._product_name},{self._product_line},{self._product_scale},{self._product_vendor},{self._product_description},\
                {self._quantity_instock}{self._buyprice}{self._msrp}'


    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, product_code):
        self._product_code = product_code

    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        self._product_name = product_name

    @property
    def product_line(self):
        return self._product_line

    @product_line.setter
    def product_line(self, product_line):
        self._product_line = product_line

    @property
    def product_scale(self):
        return self._product_scale

    @product_scale.setter
    def product_scale(self, product_scale):
        self._product_scale = product_scale

    @property
    def product_vendor(self):
        return self._product_vendor
    @product_vendor.setter

    def product_vendor(self, product_vendor):
        self._product_vendor = product_vendor
    
    @property
    def product_description(self):
        return self._product_description

    @product_description.setter
    def product_description(self, product_description):
        self._product_description = product_description
    
    @property
    def quantity_instock(self):
        return self._quantity_instock

    @quantity_instock.setter
    def quantity_instock(self, quantity_instock):
        self._quantity_instock = quantity_instock

    @property
    def _buyprice(self):
        return self.__buyprice

    @_buyprice.setter
    def _buyprice(self, _buyprice):
        self.__buyprice = _buyprice   

    @property
    def msrp(self):
        return self._msrp

    @msrp.setter
    def msrp(self, msrp):
        self._msrp = msrp 