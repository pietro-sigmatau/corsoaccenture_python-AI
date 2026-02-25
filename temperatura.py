temperature = {18, 22, 30, 12, 15, 32, 27, 19, 28, 20}

# lista temperature superiori a 20

temp_sup = []

for temp in temperature:
    if temp > 20:
        temp_sup.append(temp)

print(temp_sup)