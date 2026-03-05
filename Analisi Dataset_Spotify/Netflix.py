import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

from scipy.sparse import hstack, csr_matrix

pd.options.display.max_columns = 20

df = pd.read_csv("NetFlix.csv")

# 1) dedup come Spotify
df = df.drop_duplicates(subset=["show_id"], keep="first")

# 2) soup = director + cast + genres + description
for c in ["director", "cast", "genres", "description"]:
    df[c] = df[c].fillna("").astype(str)

df["soup"] = (
    df["director"] + " " +
    df["cast"] + " " +
    df["genres"] + " " +
    df["description"]
).str.lower()

# 3) TF-IDF
tfidf = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
X_text = tfidf.fit_transform(df["soup"])  # sparse

# 4) OHE (dummies) SOLO su type e rating
type_ohe   = pd.get_dummies(df["type"].fillna(""), prefix="type")
rating_ohe = pd.get_dummies(df["rating"].fillna(""), prefix="rating")

# multi-hot per liste tipo "United States, India" e "Dramas, Comedies"
country_mh = df["country"].fillna("").astype(str).str.get_dummies(sep=", ").add_prefix("country_")
genres_mh  = df["genres"].fillna("").astype(str).str.get_dummies(sep=", ").add_prefix("genre_")

# 5) numeriche (release_year + duration_num)
# duration è stringa tipo "90 min" / "2 Seasons" -> prendiamo il primo numero
duration_num = (
    df["duration"]
    .fillna("")
    .astype(str)
    .str.extract(r"(\d+)")[0]
    .astype(float)
    .fillna(0.0)
)

X_num = pd.DataFrame({
    "release_year": df["release_year"].fillna(0).astype(float),
    "duration_num": duration_num
})

scaler = StandardScaler()
X_num_scaled = scaler.fit_transform(X_num)

# 6) unione finale (testo + meta)  <-- QUI
X_meta_dense = np.hstack([
    X_num_scaled,
    type_ohe.values,
    rating_ohe.values
])

X_final = hstack([X_text, csr_matrix(X_meta_dense)])

# 7) NearestNeighbors (niente algorithm=...)
model = NearestNeighbors(metric="euclidean", n_neighbors=50)
model.fit(X_final)

# 8) niente .to_dict(): usiamo show_id come index
df = df.set_index("show_id", drop=False)

def recommend_by_show_id(show_id: str, k: int = 10, same_type: bool = False) -> pd.DataFrame:
    if show_id not in df.index:
        raise ValueError("show_id non trovato")

    seed_pos = df.index.get_loc(show_id)
    seed_row = df.iloc[seed_pos]

    # QUI è il punto che cambia rispetto a prima: stile Spotify (k + 1)
    distances, indices = model.kneighbors(X_final[seed_pos], n_neighbors=k + 1)

    recs = df.iloc[indices[0]].copy()
    recs = recs[recs["show_id"] != show_id]

    if same_type:
        recs = recs[recs["type"] == seed_row["type"]]

    recs = recs.head(k)

    cols = ["show_id", "title", "type", "release_year", "rating", "duration", "genres"]
    return recs[cols]

# TEST
test_id = df["show_id"].iloc[0]
test_id = "s5236"
print("Seed:")
print(df.loc[test_id, ["show_id", "title", "type"]])

print("\nRaccomandazioni:")
print(recommend_by_show_id(test_id, k=10, same_type=False))