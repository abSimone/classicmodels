class ProductLine:
    def __init__(self, productLine, textDescription, htmlDescription, image):
        self._productLine=productLine
        self._textDescription=textDescription
        self._htmlDescription=htmlDescription
        self._image=image
  
    @property
    def productLine(self):
        return self._productLine 
    
    @productLine.setter    
    def productLine(self, productLine):
        self._productLine = productLine
        
    @property
    def textDescription(self):
        return self._textDescription
    
    @textDescription.setter    
    def textDescription(self, textDescription):
        self._textDescription = textDescription
    
    @property
    def htmlDescription(self):
        return self._htmlDescription 
    
    @htmlDescription.setter    
    def htmlDescription(self, htmlDescription):
        self._htmlDescription = htmlDescription
        
    @property
    def image(self):
        return self._image 
    
    @image.setter    
    def image(self, image):
        self._image = image
    
    def __str__(self):
        return f"Linea del prodotto: {self._productLine}, Descrizione testo: {self._textDescription}, Descrizione html: {self._htmlDescription}, immagine: {self._image}"