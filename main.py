numeri = [1,2,3,4]

quadrati = []

for numero in numeri:
    quadrati.append(numero)


#%%

numeri = [1,2,3,4]
quadrati = [numero ** 2 for numero in numeri]  #LIST COMPRENSION

#trasformazione for elemento in elementi sintassi (lista di elementi...
#prendiamo un elemento e lo trasformiamo)

print(quadrati)