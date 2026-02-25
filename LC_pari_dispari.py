numeri = [5, 12, 7, 20, 3, 18]

"""
creare una lista che divida per due i numeri maggiori di 10, lasci invariati
gli altri

[A if CONDIZIONE else B for elemento in sequenza]
"""

newnumeri=[numero/2 if numero>10 else numero for numero in numeri]

print(newnumeri)