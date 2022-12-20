# File che utilizzeremo in futuro :D

from dao.productDao import Product
from dao.customersDao import CustomersDao
from dao.EmployeeDao import EmployeeDao
from dao.esercizioDao import Risoluzione

def sol_es1():
    global qry1
    office_code=input('Digitare il codice dell\'ufficio: ')
    qry1.getCustomerbyOfficecode(office_code)
    

def sol_es2():
    global qry1
    product_name=input('Digitare il nome del prodotto: ')
    qry1.getProductbyName(product_name)

def sol_es3():
    global qry1
    productline_name=input('Digitare la product line: ')
    qry1.getProductbyProductline(productline_name)

def sol_es4():
    global qry1
    productline_name=input('Digitare la product line: ')
    qry1.getProductbyProductline(productline_name)
    

qry1=Risoluzione()
selezione=int(input('(Selezionare con 1,2,3 o 4)\n1)Soluzione esercizio 1\n2)Soluzione esercizio 2\n3)Soluzione esercizio 3\n4)Soluzione esercizio 4\n--->'))
match selezione:
    case 1:
        sol_es1()
    case 2:
        sol_es2
    case 3:
        sol_es3
    case 4:
        sol_es4
    







