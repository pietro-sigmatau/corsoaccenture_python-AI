import pandas as pd

dati = {
    "nome": ["Ciccio", "Anna", "Marcello", "Francesca", "Paolo"],
    "eta": [None, 25,38,None, 21],
    "stipendio": [1200, 1800, None, 2100, None]
}

df = pd.DataFrame(dati)

print(df)

#print(df.isnull()) se va bene o no

print(df.info())

#possiamo eliminare con un solo comando le rige NaN
print(df.dropna())
#posso dirgli di andare a sostituire tutti i dati di età mancanti

#df["eta"] = df["eta"].fillna(20)

#è una best practice sostituire i dati mancanti con la media (qualora siano mancanti o da riempire)
media_eta = df["eta"].mean()
df["eta"] = df["eta"].fillna(media_eta)
media_stipendio = df["stipendio"].mean()
df["stipendio"] = df["stipendio"].fillna(media_stipendio)

"""
oppure
df["eta"]"""

print(df)