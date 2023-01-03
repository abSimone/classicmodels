class ProductLinesdto:
    def __init__(self, productLine, textdescription, html_description, image):
        self.productLine=productLine
        self.textdescription=textdescription
        self.html_description=html_description
        self.image=image

    def __str__(self):
        return f'{self._productLine} , {self._textdescription},{self._html_description},{self._image}'


    @property
    def productLine(self):
        return self._productLine

    @productLine.setter
    def productLine(self, productLine):
        self._productLine = productLine

    @property
    def textdescription(self):
        return self._textdescription

    @textdescription.setter
    def textdescription(self, textdescription):
        self._textdescription = textdescription

    @property
    def html_description(self):
        return self._html_description

    @html_description.setter
    def html_description(self, html_description):
        self._html_description = html_description

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        self._image = image