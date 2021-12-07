#realizzare un programma con le seguenti funzioni per la manipolazione di liste:
#stampa: una funzione che stampa il contenuto di una lista passata come argomento;
#statistiche: una funzione che riceve una lista e, se e' una lista di interi, ne determina la somma, media, massimo, minimo degli elementi;
#somma_vettoriale: una funzione che riceve in ingresso due liste , determina se sono due liste di interi, se hanno la stessa dimensione e ne calcola la somma vettoriale, poi ritonata come lista, altrimenti ritorna una lista vuota;
#testare le funzioni passandogli in input diverse liste
#nota: potete uare la funzione built-in type per verificare se una certa variabile e' un (oggetto) int oppure no (es: type(var int)==int -> true). Non serve importare alcun modulo

#funzione stampa
def stampa(the_list):

    #stampa la lista
    print(lista)


#funzione statistiche
def statistiche(the_list):
    
    #inizializzo la somma a 0
    somma=0

    #valuto gli elementi della lista
    for item in the_list:

        #se gli elementi sono interi #isinstance(item, int)
        if type(item)==int:

            #somma gli elementi
            somma=somma+item

            #media degli elementi con funzione len()
            media=somma/len(lista)

            #trovo il minimo valore della lista con la funzione min()
            minimo=min(lista)

            #trovo il massimo valore della lista con la funzione max()
            massimo=max(lista)


    #ritorno i valori
    print(somma)
    print(media)  
    print(minimo)
    print(massimo)


def somma_vettoriale(the_list, the_list2):

    #inizializzo una terza lista vuota
    lista3=[]

    #valuto gli elementi della prima lista
    for item in (range(len(the_list))):

        #se gli elementi sono interi nella prima lista
        if type(item)==int:

            #se le liste hanno la stessa dimensione 
            if len(the_list) == len(the_list2):

                #effettuo la somma vettoriale
                lista3=(the_list[item]+the_list2[item])

                #stampo la nuova lista
                print(lista3)

        #se queste condizioni non sono soddisfatte
        else:

            #stampo lista vuota
            print(lista3)





#definizione liste
lista=[1,2,3,4]
lista2=[4,5,6,7]

#richiamo la funzione 
risultato=stampa(lista)
risultato2=statistiche(lista)
risultato3=somma_vettoriale(lista, lista2)

#stampo i risultati
print(risultato)
print(risultato2)
print(risultato3)




    