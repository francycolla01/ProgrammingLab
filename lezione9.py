#estendete il modellao della lezione precedente IncrementModel come FitIncrementalModel, andando ad implementare il modello fit(). Il fit deve calcolare l'incremento medio su tutto il dataset e salvarlo da qualche parte (es: self.global_avg_increment).
#poi sovrascrivete il metodo predict() in modo che usi l'incremento medio su tutto il dataset 



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


