#create il vostro primo modello

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
        prediz=diff/lungh

    return prediz

data=[50,52,60]
ris=IncrementModel(data)
print(ris)
