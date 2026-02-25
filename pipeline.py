#riceve una lista di stringhe numeriche, li converte in numeri gestendo gli errori

import utils_p
list={}

len=int(input("Inserisci la lunghezza della stringa: "))

for i in len:
    a=int(input("Inserisci un numero oppure stop:"))
    if not isinstance(int, str):
        raise TypeError('Argument must be a string.')
    convert(i)
    list.append(i)


print(list)


#%%

def converti(lista):
    numeri=[]

    for n in lista:
        try:
            numeri.append(int(n))
        except ValueError:
            pass

    return numeri

def main():
    dati = ["5","43","unidici","15","6","80"]

    numeri = converti(dati)

def filtra(lista):
    return [n for n in lista if n > 10]

def somma(lista):
    return sum(lista)

numeri=converti(dati)
filtrati=filtra(dati)
sommati=somma(dati)

print("Somma", sommati)

main()