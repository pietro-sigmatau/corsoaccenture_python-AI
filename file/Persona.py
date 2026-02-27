class Persona:

    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta #self.eta=25 tutte le persone hanno 25 anni, non utile
                       #l'eta viene passsata quando si crea un oggetto(differiscedaoggettoaoggetto
        #numero_mani = 2

    def saluta(self): #passo self nel momento in cui la mia classe utilizzi le proprie info
        print(f"Ciao, mi chiamo {self.nome}, e ho {self.eta} anni e studio {self.corso}")


p1= Persona("Ciccio", 26)
p2= Persona("Francesca", 23)

print(p1.nome)
print(p1.eta)

print(type(p1))


p1.saluta()
