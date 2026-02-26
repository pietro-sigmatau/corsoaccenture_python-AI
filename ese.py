import csv
import json

#Pulizia dati

with(open("ese.csv", "r")) as f:
    nomi = f.readlines()

    utenti_puliti = []

    for n in nomi:
        nome = n.strip()
        nome = nome.title()
        nome = nome.replace("\n", "")
        utenti_puliti.append(nome)
        if nome in utenti_puliti:
            nome = nome.replace("<null>", "")

with open("dati_puliti.txt", "w") as f:
    for nome in utenti_puliti:
        f.write(nome + "\n")
        




#Seniority (colonna + risultato)
with open("ese.csv", newline='') as f_input:

    reader = csv.DictReader(f_input)

    utenti_modificati = []

    for row in reader:

     try:

        eta=int(row["eta"])


        if eta>=30:
            categoria = "Senior"

        elif eta>=18:
            categoria = "Mid"

        else:
            categoria = "Junior"

            row["categoria"]=categoria

            utenti_modificati.append(row)

     except:
         pass


with open("ese.csv", "w", newline='') as f_output:

    colonne = ["nome", "eta", "citta", "categoria"]

    writer = csv.DictWriter(f_output, fieldnames=colonne)
    writer.writeheader()
    writer.writerows(utenti_modificati)

print(utenti_modificati)
print(utenti_puliti)

