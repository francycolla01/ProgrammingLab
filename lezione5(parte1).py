#parte1

#modificate l'oggetto CSVFile della lezione precedente in modo che stampi a schermo un messaggio di errore se si cerca di aprire un file non esistente
#potete fare questo controllo nell'ambito: 
#1)nella funzione get_data() o
#2)nell'__init__() (basta che leggiate la prima riga per vedere se il file esiste)

class CSVFile():
    
    #venga inizializzato sul nome del file csv e abbia un attributo name che contenga il nome 
    def __init__(self, name):

        self.name=name
        

    #abbia un metodo get_data() che torni i dati del file CSV come lista di liste
    def get_data(self):

        #gestistico l'errore
        try:
            my_file=open(self.name, 'r')

        except:
            print('Il file non esiste! Quindi utilizza il file shampoo_sales.csv')
            my_file=open('shampoo_sales.csv', 'r')

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
my_object=CSVFile('file_inesistente.csv')

#creo una variabile my_data che assumera' il "valore" dell'oggetto che mi ritorna get_data
my_data=my_object.get_data()

#stampo a schermo il risultato di get_data
print(my_data)

