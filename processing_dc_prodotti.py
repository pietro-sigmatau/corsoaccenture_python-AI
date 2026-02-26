import csv

dataset=[]

with open("dc_prodotti.csv", newline='') as csvfile:
    reader=csv.reader(csvfile)
    writer=csv.writer(csvfile)


for riga in reader:
    writer = csv.Dictwriter(csvfil
    dataset.append(riga)