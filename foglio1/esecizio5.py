aqQ #estendere l'esercizio 4 realizzando la sottoclasse Transformer della classe Automobile. La sottoclasse e' caratterizzata dai seguenti attributi:
#nome, ossia il nome dell’istanza della classe Transformer;
#generazione, ossia la generazione di appartenenza del Transformer come un intero positivo (1, 2, 3, ...);
#grado, ossia il grado militare (es. ”soldato semplice”, ”sergente”, ”capitano”);
#reparto, ossia la divisione a cui fa parte l’istanza della classe quindi ”corpo a corpo”, ”artiglieria leggera”, ”artiglieria pesante”, ”spionaggio”, ... .
#E metodi:
#sovrascrivere il metodo init per fare in modo che accetti i nuovi attributi;
#definire il metodo scheda militare che stampa a schermo le informazioni ”militari” di una istanza della classe Transformer.
#Utilizzare super() dove lo si ritiene appropriato.


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
    def confronta(self, other):
      
#sottoclasse Transformer 
class Transformer(Automobile):

    def __init__(self, nome, generazione, grado, reparto):

        self.nome=nome
        self.generazione=generazione
        self.grado=grado
        self.reparto=reparto

    def scheda_militare(self):

        return 'Le informazioni del militare sono: "{} {} {}" '.format(self.nome, self.grado, self.reparto)
        


automobile=Automobile('Honda', 'CRV', '5 posti', 'CE567')
print(automobile)
automobile.parla()

