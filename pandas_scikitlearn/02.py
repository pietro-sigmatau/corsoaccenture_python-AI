import pandas as pd
dati = {
    "settore": ["Tech", "Retail", "Finance", "Tech", "Tech", "Retail", "Finance"],
    "dipendenti":[50, 70, 30, 90, 80, 75, 20],
    "fatturato": [50000, 60000, 33000, 120000, 90000, 85000, 18000]
}

df=pd.DataFrame(dati)

#fatturato medio per settore
#numero totale di dipendenti per settore
#settore con massimo fatturato totale

df = pd.DataFrame(dati)

print(df.groupby("settore")["fatturato"].mean())      # fatturato medio
print(df.groupby("settore")["dipendenti"].sum())      # dipendenti totali
print(df.groupby("settore")["fatturato"].sum())       # fatturato totale

settore_max = df.groupby("settore")["fatturato"].sum().idxmax()
print("Settore con massimo fatturato totale:", settore_max)