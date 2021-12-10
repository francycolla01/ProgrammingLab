#implementare una funzione (simile a quella cerata le lezioni precedenti) che ritorni una lista i cui elementi saranno le date delle vendite del file shampoo_sales.csv
#attenzione: avevate usato la funzione float per convertire i prezzi da stringhe a valori numerici. Questa volta dovrete usare un'altra funzione (vedi pdf). Questa conversione vi permettera' di eseguire operazioni con le date (come trovare la data piu' lontana, quella piu' vicina, la conversione in mesi, ecc..). Stampando la lista pero' vedrete degli oggetti del tipo DataTime. Se volete stampare la lista in modopiu' leggibile, i comandi sono i seguenti: (vedi pdf)


#apro shampoo_sales
my_file=open('foglio1/shampoo_sales.csv', 'r')

#inizializzo lista vuota dove ci sono i valori
values=[]

#scorro tutte le linee
for line in my_file:

    #creo una lista vuota
    data_vendite=[]

    elements=line.strip(',')
    #divido tra Date  ,  Sales 
    elements=line.split(',')

    #se non sono su Sales
    if elements[1]!="Sales":
      
        #importo la libreria datetime
        from datetime import datetime

        #definisco date nella stringa alla prima posizione
        date=elements[0]

        #definisco value nella stringa alla seconda posizione
        value=elements[1]

        my_date=datetime.strptime(elements[0], '%d-%m-%Y')

    for date in date_vendite:
        print(date.strftime('%d-%m-%Y'))

#chiudo il file
my_file.close()