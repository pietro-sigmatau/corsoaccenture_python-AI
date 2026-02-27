class Libro:
    def __init__(self, titolo, pagine, autore, categoria):
        self.titolo = titolo
        self.pagine = pagine
        self.autore = autore
        self.categoria = categoria

    def descrizione(self):
        print(f"{self.titolo} - num. pagine {self.pagine} - {self.autore} - {self.categoria}")


libro_1=Libro("Critica della Ragion Pura", 750, "Immanuel Kant", "Filofosia")
libro_1.descrizione()