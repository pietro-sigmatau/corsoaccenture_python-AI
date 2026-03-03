import numpy as np

studenti = np.array([
    [80,79,90],
    [60,75,90],
    [88,93,90],
    [55,68,70]
])

"""
ogni riga è uno studente
ogni colonna è una materia

media per studente
media per materia
studenti con media maggiore di 75

normalizzare il dataset
"""

#le medie

media_studenti = np.mean(studenti, axis=1)
media_materie = np.mean(studenti, axis=0)

#studenti con media > 75

studenti_bravi=media_studenti>75 #maschera bool

studenti_sopra_74 = studenti[studenti_bravi]

minimo=np.min(studenti)
massimo=np.max(studenti)

print(media_materie)
print(media_studenti)


norm=((studenti-minimo)/(massimo-minimo))

print(norm) #oss 1 è 93, quello più alto
print(studenti_bravi)
print(studenti_sopra_74)

#oss NO FILTRAGGIO CON CICLO FOR, FILTRAGGIO BOOLEANO!!