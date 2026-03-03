import numpy as np
numeri = [1,2,3,4]

#voglio moltiplicare tutto per 2
#nuovi = [n*2 for n in numeri] con list comprehension

#nuovi = []

#for n in numeri:
#    numeri.append(n*2)


array = np.array(numeri)

nuovi = array * 2
print(nuovi)

#comandi base numpy
#creare un vettore/array di n numeri randomici
numeri_random=np.random.randint(1, 101, 10) #(10 è il numero di elementi da includere nell'array finale)

print(numeri_random)

#calcolo media .mean
#calcolo massimo .max

print(np.mean(numeri_random))
print(np.max(numeri_random))