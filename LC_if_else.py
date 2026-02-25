numeri = [1,2,3,4,5,6,7,8,9]

#scelta tra due trasformazioni la struttura va a cambiare ed è un problema
#ese voglio andare a stampare una collection che mi dica se il numero è pari o dispari
#output dispari pari dispari pari

#SINTASSI: [A if CONDIZIONE else B for elemento in sequenza]
#si creano liste pari e dispari

risultato = ["pari" if numero % 2==0 else "dispari" for numero in numeri]

print(risultato)

#non usiamola con if annidati o logica complessa, quando diventa difficile da
#leggere e con debugging riga per riga, soluzione? una funzione con operazioni modulari