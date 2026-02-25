lista = {'giallo', 'verde', 'blu'}

for colore in lista:
    print(colore)

#%%

numeri = {10, 20, 30}
nuovi_numeri = []

for numero in numeri:
    nuovo = numero + 2
    nuovi_numeri.append(nuovo)

print(nuovi_numeri)

#%%

numeri = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
nuovi_numeri = []
pari = []

for numero in numeri:
    if numero % 2 == 0:
        pari.append(numero)

print(pari)

#%%

