f = open("dati.txt","r")

print(f.read())
f.close()

"""
le modalità sono
r read (lettura)
w write (scrittura e sovrascrittura)
a append (aggiunge qualcosa alla fine del file, come per gli array)
r+ (lettura+scrittura, più scomoda)

with open ecc (apre il file per leggere e richiude da solo)

mini pipeline

apertura file trasformazione lettura
"""

#%%

with(open("dati.txt","r")) as f:
    contenuto = f.read()

print(contenuto)

# %%

with(open("dati.txt", "r")) as f:
    contenuto = f.readlines()

for line in contenuto:
    print(line)

#ilcontenuto si comporta come una lista
#con readlines serve pulire perché la linea è
#testo + a capo

# %%

with(open("dati.txt", "r")) as f:
    contenuto = f.readlines()

print(contenuto)

# ilcontenuto si comporta come una lista

#%%

with(open("dati.txt", "r")) as f:
     f.write("Distruggo le informazioni")



#%%

with(open("dati.txt", "r")) as f:
     a.write("Sono un contenuto nuovo")

#%%

with(open("dati.txt","r")) as f:
    nomi=f.readlines()

    nomi_puliti=[]

    for n in nomi:
        nome=n.strip()
        nome=nome.title()
        nome=nome.replace("\n", "")
        nomi_puliti.append(nome)

print(nomi_puliti)


with open("dati_puliti.txt", "w") as f:
    for nome in nomi_puliti:
        f.write(nome + "\n")