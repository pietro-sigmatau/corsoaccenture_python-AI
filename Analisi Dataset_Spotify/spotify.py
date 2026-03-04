import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler #fa la normalizzazione in automatico
from sklearn.neighbors import NearestNeighbors


pd.options.display.max_columns = 20

df = pd.read_csv("dataset.csv")

#missing = df.isna().sum().sort_values(ascending=False)

feature_num= [
    "energy",
    "tempo",
    "valence",
    "acousticness"
]

#one hot encoding


df = df.sort_values("popularity", ascending=False)
df = df.drop_duplicates(subset=["track_id"], keep="first")

genre_ohe = pd.get_dummies(df["track_genre"], prefix="genre")

X_num=df[feature_num]
X=pd.concat([X_num, genre_ohe], axis=1)

scaler = StandardScaler()

X_num_scaled = scaler.fit_transform(X_num)

X_final=np.hstack((X_num_scaled, genre_ohe.values))


similar_track = 10

model = NearestNeighbors(
    n_neighbors=10+1,
    metric="euclidean"
)

model.fit(X_final)

#funzioni raccomandazione, dal track id ci passa canzoni simili

#oss fare la funzione prima non va bene
def reccomend_by_track_id(
        track_id: str,
        k: int = 10,
        same_genre: bool = False
) -> pd.DataFrame:
    seed = df[df["track_id"] == track_id]
    if seed.empty:
        raise ValueError("Track ID doesen't exist")

    seed_row=seed.iloc[0]

    seed_num = seed[feature_num]
    seed_num_scaled = scaler.transform(seed_num)

    seed_genre = seed_row["track_genre"]
    seed_genre_ohe = np.zeros((1, genre_ohe.shape[1]))

    genre_col_name = f"genre_{seed_genre}"

    if genre_col_name in genre_ohe.columns:
        idx = list(genre_ohe.columns).index(genre_col_name)
        seed_genre_ohe[0,idx] = 1


    seed_vec = np.hstack([seed_num_scaled, seed_genre_ohe])

    distances,indices = model.kneighbors(seed_vec)

    recs = df.iloc[indices[0]].copy()

    recs = recs[recs["track_id"] != track_id]

    if same_genre:
        recs = recs[recs["track_genre"] == seed_row["track_genre"]]

    recs = recs.head(k)

    cols = [
        "track_id",
        "track_name",
        "artists",
        "track_genre",
        "popularity"
    ]

    return[recs[cols]]

test_id = "3Zik0kcruJ6vZukE5YvVbF"

print("Traccia seed: \n")
print(df[df["track_id"] == test_id][["track_name", "artists"]])
print("Tracce c: \n")
print(reccomend_by_track_id(test_id, k=10, same_genre=False))

#print(df["track_genre"].nunique())


#print("Tracce uniche:", df["track_id"].nunique())
#print(missing)
#print(df[features].describe())
