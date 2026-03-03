#istituto credito, previsione accessione finanziamento oppure no
#eta reddito annuo, numero debiti e punteggio credito
#label che ci dirà se il prestito può essere approvato è 0 non approvato 1 approvato

import numpy as np

np.random.seed(42)

#eta reddito annuo numero debiti creditscore e approvazione
dataset = np.array([
    [25, 30000, 2, 650, 1],
    [45, 80000, 1, 720, 1],
    [35, 50000, 5, 580, 0],
    [23, 25000, 3, 600, 0],
    [52, 120000, 0, 800, 1],
    [40, 70000, 4, 610, 0]
])

#dato che ci dice, guarda che approvi il credito solo in questi casi, IMPARA quando un finanziamento viene
#approvato e decidi tu in autonomia
#in teoria è dal crediscore sopra il 650

#separiamo il dataset, in X e Y

X = dataset[:, :-1] #tutte le righe e tutte le colonne tranne l'ultima (prime 4 features)
Y = dataset[:, -1]  #tutte le righe e SOLO l'ultima colonna

minimo = np.min(X, axis=0)
massimo = np.max(X, axis=0)

#hanno shape 4 ma si adattano a X che ha shape 6 e 4

X_norm = (X-minimo)/(massimo-minimo)

print(X_norm)

#pattern decisionali nei quali il nostro LM può capire in base ai valori normalizzati delle feature
#quale potrebbe essere un pattern ideale secondo cui decidere se concedere il prestito o meno

#isoliamo le feature rilevanti, e il target
#feature engineering, creiamo la nuova feature leggibile/capibile
#colonna relativa al reddito, colonna numero 1, la seconda
#estraiamo colonna debiti, la 2

#creiamo la colonna feature rapporto debiti reddito

reddito = X[:, 1]
debito = X[:, 2]

rapporto_debiti = debito / reddito #vettore ottenuto

print(rapporto_debiti) #prossimi allo 0 abbiamo dei risultati probabilmente vicini ad 1
#rapporto debito credito alto ma il finanziamento è stato ricevuto nel primo caso, magari allucinazione banca
#aggiungiamo la feature a X norm

rapporto_debiti = rapporto_debiti.reshape(-1,1)

print(rapporto_debiti)

X_enhanced = np.hstack((X_norm,rapporto_debiti))

print(X_enhanced) #in più che il rapporto debito credito

#traintest spilt simulati

indices = np.arange(len(X_enhanced))

np.random.shuffle(indices)
#quanti elementi vanno in training, tipo l'80 percento

train_size=int(len(indices)*0.8) #numero elementi in training

#80percento indici, il resto test

train_idx = indices[:train_size]
test_idx = indices[train_size:]

#righe training feature e righe test della feature, le separo

print(train_idx)
print(test_idx) #le colonne 4 e 3 matrice di test

X_train=X_enhanced[train_idx]
X_test=X_enhanced[test_idx]

#prendiamo i risultati (label 1,0) e le selezioniamo

y_train=Y[train_idx]
y_test=Y[test_idx]

print(y_train)

#DATI NEL MODELLO DI ML IN CORSO DI ADDESTRAMENTO, PERCHé DAI DATI ESCONO I RISULTATI? UNA VOLTA
#CAPITO TESTA I RISULTATI, SE I RISUTLATI DEL TEST SONO CORRETTI HAI TROVATO UN MODELLO AFFINCHE IO POSSA DECISDERE SE DARE
#AD UN SOGGETTO UN FINANZIAMETO O MENO IN BASE AI DATI CHE SI HANNO