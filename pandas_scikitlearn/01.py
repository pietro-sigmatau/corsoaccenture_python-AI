import pandas as pd

dati = {
    "nome": ["Ciccio", "Anna", "Marcello"],
    "eta": [25,22,38],
    "citta": ["Roma", "Milano", "Firenze"]
}
#definiamo un dataframe

df = pd.DataFrame(dati)
print(df.describe())


#utenti con età minore di 30

df_filtrato=df[df["eta"]<30]

print(df_filtrato)