numeri = [3,6,9,15,18,21,24,27,30]

"""
creare un dizionario 
chiave ---> numero
valore ---> numero/3"""

dc_num={n: n/3 for n in numeri}

print(dc_num)




nomi = ["Anna","Ciccio","Francesca","Annibale"]

"""
ccreare un dizionario 
chiave->nome
valore->lungo se la lunghezza è maggiore di 5 altrimenti corto"""

dc_nomi={n: "Lungo" if len(n)>5 else "Corto" for n in nomi}

print(dc_nomi)


"""
{k: v*2 for k,v in d.items()}}
"""