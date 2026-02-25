numeri = [5, 12, 26, 30, 20, 9, 14, 209]

#creare una nuova lista solo con i numeri maggiori di 10 e divisi per due (filtraggio e trasformazione)

risultato = []

for num in numeri:
    if num > 10:
        risultato.append(num/2)

print(risultato)