import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('data/Symptom.csv').drop(['Symptom_6', 'Symptom_7', 'Symptom_8', 'Symptom_9', 'Symptom_10', 'Symptom_11', 'Symptom_12', 'Symptom_13', 'Symptom_14', 'Symptom_15', 'Symptom_16', 'Symptom_17'], axis=1)

cols = df.columns
data_flat = df[cols].values.flatten()
s = pd.Series(data_flat)
s = s.str.strip()
s = s.values.reshape(df.shape)
df = pd.DataFrame(s, columns=cols)
df = df.fillna("0")

df1 = pd.read_csv('data/Symptom Severity.csv')
known = sorted([str(x).strip() for x in df1['Symptom'].unique()])
sym2idx = {s: i for i, s in enumerate(known)}

X_l = []
y_l = []
for _, r in df.iterrows():
    vec = np.zeros(len(known))
    for x in r[1:]:
        sym = str(x).strip()
        if sym in sym2idx:
            vec[sym2idx[sym]] = 1
    X_l.append(vec)
    y_l.append(r['Disease'])

X = np.array(X_l)
y = np.array(y_l)
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X, y)

vec = np.zeros(len(known))
vec[sym2idx['high_fever']] = 1
vec[sym2idx['headache']] = 1
vec[sym2idx['runny_nose']] = 1
print("prediction:", rf.predict([vec]))
