import csv

dataset=[]

with open("datiN.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    writer = csv.writer(csvfile)

    writer.writerow(["nome", "eta", "citta", "categoria"])

    for riga in reader:

        if riga['eta']>=27:
            dataset.append(riga)

print(dataset)