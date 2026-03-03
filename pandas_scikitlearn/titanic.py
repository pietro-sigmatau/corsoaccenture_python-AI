import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot as plt

pd.options.display.max_columns = 8
pd.options.display.max_rows = 100

df = pd.read_csv("Titanic-Dataset.csv")

# NON droppare Name qui, ti serve dopo
df = df.drop(["PassengerId", "Cabin", "Ticket"], axis=1, errors="ignore")

df["IsMaleChild"] = 0
df.loc[df["Name"].str.contains("Master", na=False), "IsMaleChild"] = 1

# ora puoi droppare Name
df = df.drop(["Name"], axis=1, errors="ignore")

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
df["IsAlone"] = 0
df.loc[df["FamilySize"] == 1, "IsAlone"] = 1

df["Age0015"] = 0
df["Age1540"] = 0
df["Age4080"] = 0
df.loc[df["Age"] <= 15, "Age0015"] = 1
df.loc[(df["Age"] > 15) & (df["Age"] <= 40), "Age1540"] = 1
df.loc[df["Age"] > 40, "Age4080"] = 1

df = df.drop(["SibSp", "Parch"], axis=1, errors="ignore")
df = df.drop(["Fare"], axis=1, errors="ignore")
df = df.drop(["Age"], axis=1, errors="ignore")

df = pd.get_dummies(df, columns=["Embarked", "Sex"], drop_first=True)

X = df.drop("Survived", axis=1)
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("L'accuratezza", accuracy)

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix\n", cm)

cr = classification_report(y_test, y_pred)
print("Classification Report\n", cr)

y_train_pred = model.predict(X_train)
train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy_score(y_test, y_pred)

print("Train Accuracy", train_accuracy)
print("Test Accuracy", test_accuracy)

for feature, coef in zip(X.columns, model.coef_[0]):
    print(feature, coef)


jack = {
    "Pclass": 3,
    "Age": 20,
    "FamilySize": 1,
    "IsAlone": 1,
    "Sex_Male": 1,
    "Age0015": 0,
    "Age1540": 1,
    "Age4080": 0,
    "Embarked_Q": 0,
    "Embarked_S": 1
}


rose = {
    "Pclass": 1,
    "Age": 17,
    "FamilySize": 2,
    "IsAlone": 0,
    "Sex_Male": 0,
    "Age0015": 0,
    "Age1540": 1,
    "Age4080": 0,
    "Embarked_Q": 0,
    "Embarked_S": 1
}

char_titanic_movie = pd.DataFrame([jack, rose], index=["Jack","Rose"])
char_titanic_movie = char_titanic_movie.reindex(columns=X.columns, fill_value=0)

pred_class = model.predict(char_titanic_movie)
pred_proba = model.predict_proba(char_titanic_movie)[:,1]

results = pd.DataFrame(
    {
        "Predicted Survived": pred_class,
        "Predicted Probability": pred_proba
    }, index=char_titanic_movie.index
)

print(results)

survived_by_sex = df.groupby("Sex_male")["Survived"].mean()
plt.figure()
plt.bar(["Femminucce","Maschietti"], survived_by_sex)
plt.title("Sopravvivenza per sesso (%)")
plt.ylabel("Probabilità di sopravvivenza")
plt.show()