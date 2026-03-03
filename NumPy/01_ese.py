import numpy as np

numeri_random=np.random.randint(1, 101, 10)

mean=numeri_random.mean()
max=numeri_random.max()

nr_three=numeri_random * 3

filtered=[]

print(numeri_random)
print(mean)
print(max)
print(nr_three)

#filtro
print(numeri_random[numeri_random > 50])