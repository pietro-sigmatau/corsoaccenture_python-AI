from file.Persona import Persona

class Studente(Persona):

    def __init__(self, nome, eta, corso):
        super().__init__(nome, eta)
        self.corso = corso

    def saluta(self):
        return f"Ciao, mi chiamo {self.nome}, ho {self.eta}, e studio {self.corso}" #override

   #""" def saluta_come_una_persona_normale(self):
    #    super().saluta()"""

ciccio = Studente("Ciccio", 25, "Python AI")

print(ciccio.saluta())