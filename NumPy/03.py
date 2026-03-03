import numpy as np
x=5

v=np.array([1,2,3,4,5])

"""m=np.array(
    [1,2,3]
    [4,5,6]
    [7,8,9]
)"""

#tensore 3D

t = np.array([
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]
])

print(t.shape)


#esempio di broadcasting
#a=np.array([1,2,3,4,5])
#b=10
#a+b

a=np.array(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
)
media=np.mean(a, axis=0)
norm = a - media
b=np.array([10, 20, 30])

print(norm)

print(a+b)

""" [1,2,3,4,5] + [10,10,10,10,10]"""

#esempio reshaping
c = np.array([1,2,3,4,5,6])

d = c.reshape(3,2) #dimensioni forma che voglio ottenere
#non si può fare in questo caso il reshape di 8 tipo c.reshape(4,2)
#c.reshape(3,-1) calcola in automatico la dimensione in -1, c.reshape(-1,6)
#reshape si può fare a patto che si mantengano lo stesso numero di elementi (basta che ci sia una dimensione nota)
#reshape, machine learning

g = np.array([1,2,5,3,5,7,7,5,4,3,5,67,7,9])
l= c.reshape(2,-1)
p = g[0:2].copy() #p è una copia di g, non una referenza; prendo una slice di g, la modifico creando una copia con i soli primi due elementi
p[0] = 99
print(p)
print(g)


print(d)

#operazioni su g creando copie, mantenendo set di dati integri, molti bug nascono dal non copiare i dati iniziali
