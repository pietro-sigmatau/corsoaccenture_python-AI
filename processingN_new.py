import csv

with open("datiN.csv", newline='') as f_input:

    reader = csv.DictReader(f_input)

    utenti_modificati = []

    for row in reader:

        eta=int(row["eta"])

        if eta>=27:
            categoria = "Senior"

        else:
            categoria = "Junior"

        row["categoria"]=categoria

        utenti_modificati.append(row)


with open("dati_nuovi.csv", "w", newline='') as f_output:

    colonne = ["nome", "eta", "citta", "categoria"]

    writer = csv.DictWriter(f_output, fieldnames=colonne)
    writer.writeheader()
    writer.writerows(utenti_modificati)

print(utenti_modificati)