#parte 2

#estendete l'oggetto CSVFile chiamandolo NumericalCSVFile e facendo in modo che converta automaticamente a numero tutte le colonne tranne la prima (della data)

class CSVFile():
    
    #venga inizializzato sul nome del file csv e abbia un attributo name che contenga il nome 
    def __init__(self, name):

        self.name=name

    class NumericalCSVFile(CSVFil):

        #apro shampoo_sales
        my_file=open('shampoo_sales.csv', 'r')

        def get_data(self):

            #scorro tutte le linee
            for line in my_file:

                #divido tra Date  ,  Sales 
                elements=line.split(',')

                #se non sono su Date
                if elements[0]!="Date":
        
                    #definisco date nella stringa alla prima posizione
                    date=elements[0]

                    #definisco value nella stringa alla seconda posizione
                    value=elements[1]

                    #copio value e lo trasformo in un float
                    values.append(float(value))

                    return values

#chiudo il file
my_file.close()



#poi aggiungete questi due campi al file "shampoo_sales.csv" (vedi pdf) e gestite gli errori che verranno generati in modod che le linee vengano saltate senza bloccare il programma ma che venga stampato a scehrmo l'errore

#istanzio l'oggetto con il file shampoo_sales
my_object=CSVFile('shampoo_sales.csv')

#creo una variabile my_data che assumera' il "valore" dell'oggetto che mi ritorna get_data
my_data=my_object.get_data()

#stampo a schermo il risultato di get_data
print(my_data)