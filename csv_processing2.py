with open("dati.csv", "w", newline='') as csvfile:

    colonne=("nome","eta","citta")

    writer = csv.Dictwriter(csvfile(fieldnames))