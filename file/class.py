class Persona:
    pass


p1=Persona() #istanziare un oggetto di classe persona
p2=Persona() #nelle parentesi c'è info persona

#hanno stessi attributi e metodi pi per i da 1 a n



class int:
    pass

a= int()
a= 2
#stessa cosa di int

#metodi degli interi


#%%

#metodi per costruire una persona -> con il costruttore --init--(attributi)
#anche self/this è standard; self indica il contesto, si parla della classe essa stessa
#le funzioni, nelle classi, vengono promosse a METODI (il metodo è una funzione in una classe)

class Persona:

    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta #self.eta=25 tutte le persone hanno 25 anni, non utile
                       #l'eta viene passsata quando si crea un oggetto(differiscedaoggettoaoggetto
        #numero_mani = 2

    def saluta(self): #passo self nel momento in cui la mia classe utilizzi le proprie info
        print(f"Ciao, mi chiamo {self.nome}, e ho {self.eta} anni")


p1= Persona("Ciccio", 26)
p2= Persona("Francesca", 23)

print(p1.nome)
print(p1.eta)

print(type(p1))


p1.saluta()
p2.saluta()


