#scrivere una funzione che sommi tutti i valori delle vendite degli shampoo del file "shampoo_sales.csv". Poi committate il file in cui lo avete scritto 

#apro shampoo_sales
my_file=open('shampoo_sales.csv', 'r')

#inizializzo lista vuota dove ci sono i valori
values=[]

#inizializzo la somma = 0
s=0

#scorro tutte le linee
for line in my_file:

    #divido tra Date  ,  Sales 
    elements=line.split(',')

    #se non solo su Date
    if elements[0]!="Date":
        
        #definisco date nella stringa alla prima posizione
        date=elements[0]

        #definisco value nella stringa alla seconda posizione
        value=elements[1]

        #copio value e lo trasformo in un float
        values.append(float(value))

        #effettuo la somma ma trasformando in float tutti gli elementi al secondo posto dells stringa
        s=s+float(elements[1])

#stampo la somma
print(s)

#chiudo il file
my_file.close()


    