with(open("dati.txt", "r")) as f:



with(open("dati_puliti.txt", "w")) as f:
    f.write("\n".join(nomi_puliti))