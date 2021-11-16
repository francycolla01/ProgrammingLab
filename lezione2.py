#scrivere una funzione che sommi tutti gli elementi di una lista

#funzione somma
def somma(the_list):

    #somma iniziale uguale a 0
    s=0

    #somma gli elementi della lista
    for item in the_list:
        s=s+item

    #ritorna la somma
    return s


#definizione lista
lista=[1,2,3,4]

#richiamo la funzione
risultato=somma(lista)

#stampo il valore calcolato dalla funzione
print(risultato)
