class ProductsLines:
    def __init__(self, productLine, textDescription, htmlDescription, image):
        self.productLine = productLine
        self.textDescription = textDescription
        self.htmlDescription = htmlDescription
        self.image = image

    # getter
    @property
    def productLine(self):
        return self._productLine

    @property
    def textDescription(self):
        return self._textDescription

    @property
    def htmlDescription(self):
        return self._htmlDescription

    @property
    def image(self):
        return self._image

    # setter

    @productLine.setter
    def productLine(self, productLine):
        self._productLine = productLine
        
    @htmlDescription.setter
    def htmlDescription(self, htmlDescription):
        self._htmlDescription = htmlDescription

    @textDescription.setter
    def textDescription(self, textDescription):
        self._textDescription = textDescription

    @image.setter
    def image(self, image):
        self._image = image

    def __str__(self):
        return f"linea prodotto: {self._productLine}, descrizione: {self._textDescription}, descrizione html: {self._htmlDescription}, immagine: {self._image}"