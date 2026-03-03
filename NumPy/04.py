#Simulazione Dataset AI
import numpy as np

dataset = np.random.uniform(0,100, (5,4))
#ogni riga persona, 5 persone con 4 feature ciascuna
#eta, altezza, peso, punteggio
#normalizziamo solamente le ultime tre colonne
#aggiungiamo una nuova colonna con media delle features, creare una copia del dataset prima di modificarlo
#modificare che la copia non sia alterata
print(dataset)

#copia di sicurezza, la lasciamo da parte e lavoriamo sul dataset originale

dataset_originale=dataset.copy()

#normalizziamo solamente le ultime 3 colonne, indice 1 2 e 3

features_ds = dataset[:, 1:] #righe dalla prima all'ultima e le colonne dall'indice 1 in poi

#normalizzazione

minimo = np.min(features_ds, axis=0)
massimo = np.max(features_ds, axis=0)

features_norm = (features_ds - minimo)/(massimo - minimo)

print(features_norm)

#sostituisco il dataset iniziale

dataset[:, 1:] =features_norm

print(dataset)


print(features_ds)

#media delle feature per ogni riga

media_feature=np.mean(dataset[:, 1:], axis=1) #axis=1 è sulle righe
media_feature=media_feature.reshape(-1, 1) #reshape in una sola colonna
print(media_feature)

#andiamo ad aggiungere la nuova colonna delle medie parziali al dataset

dataset_con_media=np.hstack((dataset, media_feature)) #horizontal stack (a questo, aggiungo questo)

print(dataset_con_media)

