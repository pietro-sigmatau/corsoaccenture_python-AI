with(open("dati.txt", "r")) as f:
    nomi = f.readlines()

    nomi_puliti = []

    for n in nomi:
        nome = n.strip()
        nome = nome.title()
        nome = nome.replace("\n", "")
        nomi_puliti.append(nome)

print(nomi_puliti)

with open("dati_puliti.txt", "w") as f:
    for nome in nomi_puliti:
        f.write(nome + "\n")