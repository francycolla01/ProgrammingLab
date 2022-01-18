#Create quindi la classe MovingAverage, che venga inizializzata con la lunghezza delle finestra, e che abbia un metodo compute che prenda in input la lista di valori della serie e che ritorni la lista di valori corrispondente alla media mobile.

class ExamException(Exception):
    pass


class MovingAverage():

    def __init__(self, finestra):

        self.finestra=finestra

    def compute(self, value):

        #creo una lista vuota che conterra' il risultato
        risultati=[]

        #inizializzo la somma e la media a 0
        somma=0
        media=0

        for i in range(0, len(value)-self.finestra+1):

            for k in range(i, i+self.finestra):

                somma=somma+value[k]

            media=somma/self.finestra
            risultati.append(media)
            somma=0

        return risultati



#moving_average = MovingAverage(2)

#result = moving_average.compute([2,4,8,16])

#print(result) # Deve stampare a schermo [3,6,12]
