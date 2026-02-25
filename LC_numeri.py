#LIST COMPREHENSION

numeri= [10, 20, 30]
#aggiungi 5 ad ogni numero
nuovi = [numero + 5 for numero in numeri]

print(nuovi)

#filtrare con le list comprehension

# [trasformazione for elemento in elementi if condizione]

numeri_2 = [1,2,3,4,5,6,7,8,9]

numeri_pari= [numero for numero in numeri_2 if numero % 2==0]
print(numeri_pari)
print(numeri_2)

#trasformazione più filtraggio
#numeri pari moltiplicati per 10

numeri_pari_x_10 = [numero*10 for numero in numeri_2 if numero %2==0]
#OSS LEGGE DA DESTRA VERSO SINISTRA
print(numeri_pari_x_10)
