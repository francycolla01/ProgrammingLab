#estendere la classe CSVFile che avete creato la scorsa lezione, aggiungendo i seguenti metodi:
#1. get_data_vendite(): questa funzione ritornera' una lista con le date delle vendite (hint: usare la funzione creata nell'esercizio 2)
#2 __str__(): questa funzione ritornera' l'intestazione (header) del file CSV


class CSVFile():
    
    #venga inizializzato sul nome del file csv e abbia un attributo name che contenga il nome 
    def __init__(self, name):

        self.name=name

    #abbia un metodo get_data() che torni i dati del file CSV come lista di liste
    def get_data(self):

        #apro l'attributo name 
        my_file=open(self.name, 'r')

        #inizializzo lista vuota dove ci sono i valori
        values=[]

        #scorro tutte le linee
        for line in my_file:

            #divido tra Date  ,  Sales 
            elements=line.split(',')

            #aggiungo alla lista vuota le "liste piccole" create prima
            values.append(elements)

        #chiudo il file
        my_file.close()

        #ritorno la lista
        return values


#istanzio l'oggetto con il file shampoo_sales
my_object=CSVFile('shampoo_sales.csv')

#creo una variabile my_data che assumera' il "valore" dell'oggetto che mi ritorna get_data
my_data=my_object.get_data()

#stampo a schermo il risultato di get_data
print(my_data)