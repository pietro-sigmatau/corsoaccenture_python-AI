import pandas as pd

dati = {
    "nome": ["Ciccio", " anna", "Marcello", "Francesca", "PAOLO"],
    "email": ["ciccio@email.com", "anna@email.com", "marcello@redyard.com", "Francesca.com", None],
    "eta": [23, 25,38,20, 21],
    "stipendio": [1200, 1800, 1900, 2100, 2000],
    "citta":["Roma", "Milano", "Firenze", "Roma", "Roma"],
    "categoria":["A","A","B","A","B"],
    "vendite":[240,250,190,310,370]
}

df = pd.DataFrame(dati)
df["nome"] = df["nome"].str.strip()
df["nome"] = df["nome"].str.title()
df["email"] = df["email"].str.strip()
df["email"] = df["email"].str.lower()
df["email"] = df["email"].fillna(df["email"] == "email mancante")
#df = df.dropna(subset=["email"])
#df = df[df["email"].str.contains("@")]
df["eta"] = pd.to_numeric(df["eta"], errors="coerce")
#df = df.dropna(subset=["eta"])
df["stipendio"] = df["stipendio"].fillna(df["stipendio"].mean())
df["eta"] = df["eta"].fillna(df["eta"].mean())
#df["eta"] = df["eta"].astype(int)

#raggruppare vendite per città
df=(df.groupby("citta")["vendite"].sum())
df=(df.groupby(["citta","categoria"])["vendite"].sum())

print(df)

