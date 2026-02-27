import csv
import json

class Validator:


    def validator(self, row: dict):
        # nome non vuoto
        nome = (row.get("nome", "") or "").strip()
        if nome == "":
            return False

        # eta >= 18
        eta_raw = (row.get("eta", "") or "").strip()
        try:
            eta = int(eta_raw)
        except ValueError as e:
            return False  # eta non è un numero => scarta
        if eta < 18:
            return False

        email = (row.get("email", "") or "").strip()
        if not "@" in email:
            return False



        return True



validator = Validator()
righe_valide = []

with open("requests.csv", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        if not validator.validator(row):
            continue  # <-- scarta la riga

        righe_valide.append(row)

print(righe_valide)




try:
    with open("valid_users.json", "w") as f_valid_users_json:
        json.dump(righe_valide, f_valid_users_json)

except Exception as e:
    print(e)



print("Righe valide:", len(righe_valide))







