import numpy as np
from pyexpat import features

dati = np.array([
    [34,167,70],
    [37,185,92],
    [22,173,65]
])
#matrice eta altezza peso

print(dati)
print(dati.shape) # matrice nxm

#tutte righe colonna 0
eta = dati[:, 0]

print(dati[:, 0])  #solo colonna di tutte le eta

#media della colonna

media = np.mean(dati, axis=0) #media per colonna
#media per riga è, media = np.mean(dati, axis=1)
#colonna è features, riga è record
print(media)