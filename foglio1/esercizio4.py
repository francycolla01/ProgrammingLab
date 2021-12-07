#implementare una classe Automobile che presenta i seguenti attributi: casa_automo, modello, numero_posti, targa
#inoltre la Classe deve contenere i seguenti metodi: 
#1. __init__, metodo per inizializzare una istanza della classe;
#2. __str__, metodo che stampa tutte le informazioni associate ad una specifica istanza (aka oggetto) della classe Automobile
#3. parta, metodo che stampa a schermo "Broom Broom"
#4. confronta, metodo che, data in ingresso un'altra istanza di Automobile, determina se i due oggetti hanno le stesse informazioni (eccetto per la targa che e' univoca)

#implemento classe
class Automobile():

    #metodo __init__
    def __init__(self, casa_automo, modello, numero_posti, targa):

        #attributi
        self.casa_automo=casa_automo
        self.modello=modello
        self.numero_posti=numero_posti
        self.targa=targa

    #metodo __str__
    def __str__(self):

        return 'Le informazioni Automobile sono: "{} {} {} {}" '.format(self.casa_automo, self.modello, self.numero_posti, self.targa)

    #metodo parla
    def parla(self):

        print('Broom Broom')

    #metodo confronta usando 
    def __cmp__(self, other):




        

        


automobile=Automobile('Honda', 'CRV', '5 posti', 'CE567')
print(automobile)
automobile.parla()
