#modificate l'oggetto CSVFile della lezione precedente in modod che alzi una eccezione se il nome del file non e' una stringa
#poi, modificate la funzione get_data di CSVFile i modo da leggere solo un intervallo di righe del file, aggingendo gli argomenti start ed end opzionali, controllandone la correttezza e sanitizzandoli se serve
#get_data(self, start=None, end=None)

class CSVFile():
    
    #venga inizializzato sul nome del file csv e abbia un attributo name che contenga il nome 
    def __init__(self, name):

        self.name=name

        #alzo eccezione
        if not isinstance(name, str):
            raise Exception('Il nome del file non è una stringa')

    #abbia un metodo get_data() che torni i dati del file CSV come lista di liste
    def get_data(self, start=None, end=None):

        #apro l'attributo name 
        my_file=open(self.name, 'r')

        if start is not None:
            print('Start deve valere None, da ora in poi varrà None')
            start=None

        if end is not None:
            print('End deve valere None, da ora in poi varrà None')
            end=None

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