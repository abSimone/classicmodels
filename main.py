from dao.esercizioDao import Risoluzione


def sol_es1():
    global qry1
    officecode=input('Digitare il codice dell\'ufficio: ')
    qry1.getCustomerbyOfficecode(officecode)
    

def sol_es2():
    global qry1
    productline_name=input('Digitare il nome della product line: ')
    qry1.getOrdersbyProductline(productline_name)

def sol_es3():
    global qry1
    nome=input('Digitare il nome dell\'impiegato: ')
    cognome=input('Digitare il cognome dell\'impiegato: ')
    qry1.getOrdersbyEmployee(nome, cognome)
    
def sol_es4():
    global qry1
    nome=input('Nome del cliente: ')
    cognome=input('Cognome del cliente: ')
    qry1.getOrderNumberbyCustomerdetails(nome,cognome)

def insertProductindb():
    global qry1
    codice_prodotto=input('Codice Prodotto: ')
    nome_prodotto=input('Nome Prodotto: ')
    linea_prodotto=input('Linea: ')
    scala_prodotto=input('Scala Prodotto: ')
    venditore=input('Venditore: ')
    descrizione_prodotto=input('Descrizione: ')
    quantità=input('Quantità: ')
    prezzo=input('Prezzo: ')
    msrp=input('Msrp: ')
    qry1.insertProduct(codice_prodotto, nome_prodotto, linea_prodotto, scala_prodotto,venditore, descrizione_prodotto,quantità,prezzo,msrp)

def deleteProduct():
    global qry1
    id_prodotto=input('Inserisci il codice del prodotto: ')  
    qry1.deleteFromProductsbyID(id_prodotto)

def updateProduct():
    global qry1
    id_prodotto= input('Inserisci il codice del prodotto: ')
    nome=input('Inserisci il nuovo nome del prodotto: ')
    qry1.updateProductNamebyID(nome, id_prodotto)

qry1=Risoluzione()
selezione=int(input('(Selezionare con 1,2,3 o 4)\n1)Soluzione esercizio 1\n2)Soluzione esercizio 2\n3)Soluzione esercizio 3\n4)Soluzione esercizio 4\n--->'))
match selezione:
    case 1:
        sol_es1()
    case 2:
        sol_es2()
    case 3:
        sol_es3()
    case 4:
        sol_es4()
    case 5:
        insertProductindb()
    case 6:
        deleteProduct()
    case 7:
        updateProduct()






