#valutate i due modelli visti nella lezione 8 e 9, ovvero quello senza fit (IncrementalModel) e quello con il fit (FItIncrementalModel) sui dati delle vedite dello shampoo
#Per valutare i due modelli bisognava dividere il dataset delle vendite degli shampoo in 24 mesi di dati di fit (che non servono per il modello senza fit della lezione 8, ma su cui invece va fatto il fit del modelo di lezione 9) e in 12 mesi di dati per la valutazione,su cui poi applicare entrambi i modelli e calcolare i rispettivi errori medi.

class IncrementModel():

    def __init__(self, data):
        self.data=data

    def predict(self, data):

        #varaibile che ha il valore precente
        prev_value=None

        #se la lughezza di data e' <2
        if len(data) < 2:

            print('non posso costruire una stima con solo due valori')


        #valuto i valori di ogni n
        for item in data:

            if prev_value is not None:

                #effettuo la differenza tra il primo valore del data e prev_value (che inizialmente vale 0)
                diff=item-prev_value

            #faccio assumere a prev_value il valore dell'item appena sottratto
            prev_value=item

        #calcola la lunghezza di data tranne l'ultimo
        lungh=(len(data))-1 

        #trovo la predizione
        prediz=(diff/lungh) + prev_value

class FitIncrementalModel(IncrementModel):

    def fit(self, data2):

        #varaibile che ha il valore precente
        prev_value2=None


        #se la lughezza di data e' <2
        if len(data2) < 2:

            print('non posso costruire una stima con solo due valori')

        #valuto i valori di ogni n
        for item in data2:

            if prev_value is not None:


                #effettuo la differenza tra il primo valore del data e prev_value (che inizialmente vale 0)
                diff2=item-prev_value2

            #faccio assumere a prev_value il valore dell'item appena sottratto
            prev_value=item

        #calcola la lunghezza di data tranne l'ultimo
        lungh2=(len(data))-1 

        self.global_avg_increment=diff2/lungh2

    def predict():
        
        risultato=super().predict(self.data)

        prev_fi=(((risultato-self.data[-1])+self.global_avg_increment)/2)+self.data[-1]

        return prev_fi



data=[50,52,60]
data2=[8,19,31,41]
ris=IncrementModel(data)
ris2=FitIncrementalModel(data2)
print(ris.predict(data))
print(ris2.predict())

#estrapolo alcuni dati di shampoo_sales in una lista
shampoo_sales = [266.0, 145.9, 183.1, 119.3, 180.3, 168.5, 231.8, 224.5, 192.8, 122.9, 336.5, 185.9, 194.3, 149.5, 210.1, 273.3, 191.4, 287.0, 226.0, 303.6, 289.9, 421.6, 264.5, 342.3, 339.7, 440.4, 315.9, 439.3, 401.3, 437.4, 575.5, 407.6, 682.0, 475.3, 581.3, 646.9]

# Definiscxo quanti mesi usare per la valutazione che verranno sottratti al dataset nel caso del fit
mesi=12
mesi_tagliati=len(shampoo_sales)-mesi

#istanzio un modello senza il fit
no_fit=IncrementModel()
#istanzio un modello senza fit
si_fit=FitIncrementalModel()

# Fitto sui dati fino al mese tagliato
si_fit.fit(shampoo_sales[0:mesi_tagliati])

#creo una nuova lista con entrambi i modelli
modello_new=[no_fit, si_fit]

#creo varaibile che sara' falsa, quando diventera' vera chiudero' tutto
variabile = False

#valuto i modelli
for model in modello:

    error = 0
    print('Evaluating model "{}"'.format(model))

    # Predizioni sul dataset di "valutazione" ovvero le vendite dello shampoo dal mese di cutoff in poi
    predictions = []
    for i in range(mesi):
        predict_data = shampoo_sales[mesi_tagliati+i-3-1:mesi_tagliati+i-1]
        prediction = model.predict(predict_data)
        real = shampoo_sales[mesi_tagliati+i]
        print('"{}" (pred) vs "{}" (real)'.format(int(prediction), int(real)))

        # Aggiungo se volessi poi plottare
        predictions.append(prediction)

        error += abs(prediction - shampoo_sales[mesi_tagliati+i])
    
    error = error / mesi

    print('Average error: "{}"\n'.format(error))
