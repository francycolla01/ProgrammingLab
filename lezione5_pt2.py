#parte 2

#estendete l'oggetto CSVFile chiamandolo NumericalCSVFile e facendo in modo che converta automaticamente a numero tutte le colonne tranne la prima (della data)

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



class NumericalCSVFile(CSVFile):
    
    '''if elements[0]!="Date":
        
        #definisco date nella stringa alla prima posizione
        date=elements[0]

        #definisco value nella stringa alla seconda posizione
        value=elements[1]

        #copio value e lo trasformo in un float
        values.append(float(value))'''

   def get_data

#poi aggiungete questi due campi al file "shampoo_sales.csv" (vedi pdf) e gestite gli errori che verranno generati in modod che le linee vengano saltate senza bloccare il programma ma che venga stampato a scehrmo l'errore

#istanzio l'oggetto con il file shampoo_sales
my_object=CSVFile('shampoo_sales.csv')

#creo una variabile my_data che assumera' il "valore" dell'oggetto che mi ritorna get_data
my_data=my_object.get_data()

#stampo a schermo il risultato di get_data
print(my_data)