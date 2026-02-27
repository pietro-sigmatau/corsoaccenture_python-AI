import csv
import json

#funzione validazione (che le righe ci siano tutte, cioè tutti gli elementi)
def validate_row(row):

    try:
        if not row["nome"].strip():
            return False, "Nome Mancante"
        if not row["citta"].strip():
            return False, "Città Mancante"

        eta = int(row["eta"])

        if eta < 0:
            return False, "Età non valida"

        return True, None
    except KeyError as e:
        return False, e

    except ValueError as e:
        return False, e

    except Exception as e:
        return False, e

#calcolo categoria
def calculate_category(age):
    if age < 26:
        return "Junior"
    elif age < 30:
        return "Mid"
    else:
        return "Senior"

valid_users = []

#pipeline

try:
    with open("users.csv", newline="") as f_input: \
         open("valid_users.csv", "w", newline="") as f_valid_users: \
         open("invalid_users.csv", "w", newline="") as f_invalid_users: \

    reader=csv.DictReader(f_input)

    valid_fieldnames = reader.fieldnames + ("Categoria")
    invalid_fieldnames =reader.fieldnames + ("Errore")

    valid_writer = csv.DictWriter(f_valid_users, fieldnames=valid_fieldnames)
    invalid_writer = csv.DictWriter(f_invalid_users, fieldnames=invalid_fieldnames)

    for row in reader:

        is_valid, error= validate_row(row)

        if is_valid:

            eta=int(row("eta"))
            category = calculate_category(eta)
            row["category"]= category

            valid_writer.writerow(row)

            f_valid_users.append{
                "nome":row["nome"]
                "citta":row["citta"]
                "eta":eta
                "category":category
            }

        else:
            row["errore"]= error
            invalid_writer.writerow(row)

except FileNotFoundError:
    print("File not exist")
except Exception as e:
    print(e)

#salvataggio file JSON

try:
    with open("valid_users.json", "w") as f_valid_users_json:
        json.dump(f_valid_users, f_valid_users_json) indent=4

except Exception as e:
    print(e)


print("Done.")



