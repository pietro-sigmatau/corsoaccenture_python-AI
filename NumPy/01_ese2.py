import numpy as np

punteggi = np.array([23, 46, 78, 19, 54, 28, 74, 20, 67])

media = np.mean(punteggi) #aggregatrice, restituisce un singolo punto

#print(type(media)) #float64, gestito da numpy
#print(type(punteggi))

sopra_media = punteggi > media #maschera booleana, non fa un true false singolo

print(media)
print(type(sopra_media))
print(sopra_media) #maschera booleana elemento per elemento (ciò che è sopra 45 e ciò che non lo è)

#voti sopra la media, conteggio true

numero_sopra_media = np.sum(sopra_media)
print(numero_sopra_media)

#percentuale studenti sopra la media

pc = (numero_sopra_media / len(punteggi)) * 100

print(pc) #55% degli studenti ha un voto sopra la media

#calcolo statistica descrittiva, condizioni sui vettori e filtraggio tramite maschere booleane
#queste tre cose sono il DNA della data analysis, nel ML succedono sempre
#applichiamo la formula della normalizzazione
#troviamo il minimo

minimo = np.min(punteggi)
maximo = np.max(punteggi)

normalizzati= ((punteggi-minimo)/(maximo-minimo))
print(normalizzati)
