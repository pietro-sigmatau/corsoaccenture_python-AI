import json

#Apriamo File JSON

with open("utenti.json","r") as f_in:
    utenti = json.load(f_in)

    for u in utenti:
        eta=u["eta"]

        if eta > 27:
            u["categoria"]="Senior"

        else:
            u["categoria"]="Junior"


with open("utenti_classificati.json") as f_out: