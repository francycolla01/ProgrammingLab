#Create quindi la classe Diff, che:
#quando viene inizializzata accetti anche un parametro opzionale di nome ratio il cui valore di default sia 1, e che
#abbia un metodo compute che prenda in input una lista di valori numerici e che ritorni in output la lista corrispondente alle loro differenze.

class ExamException(Exception):
    pass

class Diff():

    def __init__(self, ratio=1):

        self.ratio=ratio

    def compute(self, value):

        #creo una lista vuota che conterrà i risultati
        risultati=[]

        #se la lista è vuota
        if value is None:

            raise ExamException('la lista è vuota, non posso effettuare la differenza')

        #se la lista non e' una lista
        if not isinstance(value, list):

            raise ExamException('il valore passato non è una lista')

        #controllo che gli elementi della lista siano int e/o float 
        for item in value:

            if not (isinstance(item, int) or isinstance(item, float)):

                raise ExamException('non ho ricevuto un numero intero o float, questo numero è: "{}"'.format(item))

        #se la lunghezza è più piccola di 2
        if len(value)<2:

            raise ExamException('la lista non contiene abbastanza elementi per effettuare la differenza')

        for i in range(0, len(value)-1):

            differenza=(value[i+1]-value[i])/self.ratio

            risultati.append(differenza)
            
        return risultati

#diff = Diff()
#result = diff.compute([2,4,8,16])
#print(result) # Deve stampare a schermo [2,4,8]