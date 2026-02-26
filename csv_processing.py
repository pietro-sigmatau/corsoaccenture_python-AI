import csv

dataset=[]
with open("dati.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    writer = csv.writer(csvfile)

    writer.writerow(["nome","eta","citta"])
    writer.writerow(["Ciccio","19","Ancona"])
    #reader =csv.reader(csvfile) mette tutto in maniera diversa

    for riga in reader:
        dataset.append(riga)

#oss anche i numeri sono stringa