import sys
sys.path.append('.')
from services.nlp_service import extract_symptoms
from ml import model
model._load_and_train()

phrases = [
    "I have been feeling very itchy and have a skin rash",
    "I have terrible chest pain, breathlessness, and I am sweating a lot",
    "I've got a headache, fever, and a runny nose",
    "I have abdominal pain, diarrhea, and vomiting",
    "I feel dizzy and have a severe headache",
]

for p in phrases:
    syms = extract_symptoms(p, model.get_known_symptoms())
    res = model.predict(syms['normalized'])
    print(f"Phrase: '{p}'")
    print(f"Symptoms extracted: {syms['normalized']}")
    print(f"Prediction: {res['disease']}")
    print("-" * 50)
