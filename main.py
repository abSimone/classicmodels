# File che utilizzeremo in futuro :D

from dao.productDao import Product
def id_product_list():
    global qry1
    id_prodotto=input('Digitare l\'id del prodotto: ')
    qry1.getProductbyID(id_prodotto)
    

def product_research():
    global qry1
    product_name=input('Digitare il nome del prodotto: ')
    qry1.getProductbyName(product_name)

def productline_research():
    global qry1
    productline_name=input('Digitare la product line: ')
    qry1.getProductbyProductline(productline_name)
    

qry1=Product()
selezione=int(input('(Selezionare con 1,2 o 3)\n1)Prodotti Disponibili\n2)Cerca tramite ID del prodotto\n3)Ricerca prodotto specifico tramite il nome\n4)Rocerca prodotto per Linea\n--->'))
match selezione:
    case 1:
        qry1.getAllProduct()
    case 2:
        id_product_list()
    case 3:
        product_research()
    case 4:
        productline_research()
    







