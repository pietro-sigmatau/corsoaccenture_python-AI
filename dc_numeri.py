#dizionario è il seguente

studente = {
    "nome":"Anna",
    "eta": 22,
    "corso":"Python"
}

#se la lista è una sequenza di oggetti

num = {10,20,30}
#c'è una grande differenza di chiavi
num_d = {
    "a":10,
    "b":20,
    "c":30
}
#creiamo un dizionario a partire da una lista
#se ho una lista numeri con il dizionario che è il doppio

quadrati = {}

for n in num:
    quadrati[n]=n*n

print(quadrati)

#in modo comprehension

quadrati_c={n: n * n for n in num}

print(quadrati_c)

"""
{chiave : valore for elemento in sequenza}
per ogni iterazione del ciclo for c'è coppia di chiave valore, identica alla list compehension
"""
