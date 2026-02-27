import csv
import json


# -------------------------
# 1) Classe Richiesta
# -------------------------
class Richiesta:
    def __init__(self, nome, email, eta, servizio, categoria_eta):
        self.nome = nome
        self.email = email
        self.eta = eta
        self.servizio = servizio
        self.categoria_eta = categoria_eta

    def to_dict(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "eta": self.eta,
            "servizio": self.servizio,
            "categoria_eta": self.categoria_eta
        }


# -------------------------
# 2) Classe Validator
# -------------------------
class Validator:
    def sanitize_text(self, text):
        # toglie spazi all'inizio/fine + riduce spazi multipli
        text = (text or "").strip()
        text = " ".join(text.split())
        return text

    def sanitize_nome(self, nome):
        nome = self.sanitize_text(nome)
        return nome.title()  # "mARio rOSsi" -> "Mario Rossi"

    def sanitize_email(self, email):
        email = self.sanitize_text(email)
        email = email.replace(" ", "")  # se per caso ci sono spazi in mezzo
        return email.lower()

    def sanitize_servizio(self, servizio):
        servizio = self.sanitize_text(servizio)
        return servizio.title()

    def categoria_eta(self, eta):
        # 18–25 -> Junior
        # 26–40 -> Adult
        # >=40 -> Senior (interpretiamo così la consegna)
        if 18 <= eta <= 25:
            return "Junior"
        elif 26 <= eta <= 39:
            return "Adult"
        else:
            return "Senior"

    def is_valid(self, row):
        # 1) sanifica
        nome = self.sanitize_nome(row.get("nome", ""))
        email = self.sanitize_email(row.get("email", ""))
        servizio = self.sanitize_servizio(row.get("servizio", ""))

        # 2) valida nome
        if nome == "":
            return False

        # 3) valida email
        if "@" not in email:
            return False

        # 4) valida eta
        eta_raw = self.sanitize_text(row.get("eta", ""))
        try:
            eta = int(eta_raw)
        except ValueError:
            return False
        if eta < 18:
            return False

        # 5) servizio non vuoto (serve per set + conteggio)
        if servizio == "":
            return False

        return True

    def build_richiesta(self, row):
        # costruisce la Richiesta già sanificata + con categoria_eta
        nome = self.sanitize_nome(row.get("nome", ""))
        email = self.sanitize_email(row.get("email", ""))
        servizio = self.sanitize_servizio(row.get("servizio", ""))

        eta_raw = self.sanitize_text(row.get("eta", ""))
        eta = int(eta_raw)

        cat = self.categoria_eta(eta)
        return Richiesta(nome, email, eta, servizio, cat)


# -------------------------
# 3) Classe Pipeline
# -------------------------
class Pipeline:
    def __init__(self, input_csv, output_json):
        self.input_csv = input_csv
        self.output_json = output_json
        self.validator = Validator()

    def run(self):
        richieste_valide = []

        # 1) leggi csv + 2) valida/scarta + 3) sanifica + 4) categoria_eta
        with open(self.input_csv, newline="") as f:
            reader = csv.DictReader(f)

            for row in reader:
                if not self.validator.is_valid(row):
                    continue  # scarta la riga

                richiesta = self.validator.build_richiesta(row)
                richieste_valide.append(richiesta)

        # 5) organizzazione dati
        servizi_unici = list({r.servizio for r in richieste_valide})
        servizi_unici.sort()

        conteggio_servizi = {}

        for r in richieste_valide:
            servizio = r.servizio
            if servizio in conteggio_servizi:
                conteggio_servizi[servizio] += 1
            else:
                conteggio_servizi[servizio] = 1

        # 7) salva json nella struttura richiesta
        payload = {
            "totale_richieste": len(richieste_valide),
            "servizi_unici": servizi_unici,
            "conteggio_servizi": conteggio_servizi,
            "richieste": [r.to_dict() for r in richieste_valide]
        }

        with open(self.output_json, "w") as out:
            json.dump(payload, out, indent=4)


# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":
    p = Pipeline("requests.csv", "output.json")
    p.run()
    print("Creato output.json")