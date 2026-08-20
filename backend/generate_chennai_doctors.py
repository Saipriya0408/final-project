import json
import random
import uuid

HOSPITALS = [
    {
        "id": "hosp_001",
        "name": "Apollo Hospitals, Greams Road",
        "lat": 13.0617,
        "lng": 80.2542,
        "city": "Chennai",
        "address": "21, Greams Lane, Off Greams Road, Chennai - 600006",
        "phone": "044-28293333",
        "rating": 4.8,
        "emergency": True
    },
    {
        "id": "hosp_002",
        "name": "MIOT International",
        "lat": 13.0189,
        "lng": 80.1834,
        "city": "Chennai",
        "address": "4/112, Mount Poonamallee Road, Manapakkam, Chennai - 600089",
        "phone": "044-42002288",
        "rating": 4.7,
        "emergency": True
    },
    {
        "id": "hosp_003",
        "name": "SIMS Hospital, Vadapalani",
        "lat": 13.0505,
        "lng": 80.2119,
        "city": "Chennai",
        "address": "No 1, Jawaharlal Nehru Salai, Vadapalani, Chennai - 600026",
        "phone": "044-20002001",
        "rating": 4.6,
        "emergency": True
    },
    {
        "id": "hosp_004",
        "name": "Fortis Malar Hospital, Adyar",
        "lat": 13.0125,
        "lng": 80.2581,
        "city": "Chennai",
        "address": "No. 52, 1st Main Road, Gandhi Nagar, Adyar, Chennai - 600020",
        "phone": "044-42892222",
        "rating": 4.5,
        "emergency": True
    },
    {
        "id": "hosp_005",
        "name": "Kauvery Hospital, Alwarpet",
        "lat": 13.0336,
        "lng": 80.2562,
        "city": "Chennai",
        "address": "No. 199, Luz Church Road, Alwarpet, Chennai - 600004",
        "phone": "044-40006000",
        "rating": 4.8,
        "emergency": True
    },
    {
        "id": "hosp_006",
        "name": "Sri Ramachandra Medical Centre",
        "lat": 13.0392,
        "lng": 80.1506,
        "city": "Chennai",
        "address": "No. 1, Ramachandra Nagar, Porur, Chennai - 600116",
        "phone": "044-45928500",
        "rating": 4.9,
        "emergency": True
    },
    {
        "id": "hosp_007",
        "name": "Global Hospitals, Perumbakkam",
        "lat": 12.9038,
        "lng": 80.2010,
        "city": "Chennai",
        "address": "439, Cheran Nagar, Perumbakkam, Chennai - 600100",
        "phone": "044-44770000",
        "rating": 4.6,
        "emergency": True
    },
    {
        "id": "hosp_008",
        "name": "Vijaya Hospital, Vadapalani",
        "lat": 13.0485,
        "lng": 80.2098,
        "city": "Chennai",
        "address": "No. 323, NSK Salai, Vadapalani, Chennai - 600026",
        "phone": "044-23651234",
        "rating": 4.4,
        "emergency": True
    },
    {
        "id": "hosp_009",
        "name": "Prashanth Hospital, Velachery",
        "lat": 12.9806,
        "lng": 80.2227,
        "city": "Chennai",
        "address": "No. 36 & 36A, Velachery Main Road, Velachery, Chennai - 600042",
        "phone": "044-46805544",
        "rating": 4.5,
        "emergency": True
    },
    {
        "id": "hosp_010",
        "name": "Dr. Mehta's Hospitals, Chetpet",
        "lat": 13.0722,
        "lng": 80.2372,
        "city": "Chennai",
        "address": "No. 2, McNichols Road, 3rd Lane, Chetpet, Chennai - 600031",
        "phone": "044-42271001",
        "rating": 4.7,
        "emergency": True
    }
]

SPECIALTIES = [
    "Dermatologist", "Allergist", "Gastroenterologist", "Hepatologist",
    "Primary Care Provider", "Endocrinologist", "Pulmonologist", 
    "Cardiologist", "Neurologist", "Orthopedic", "Neurosurgeon",
    "Infectious Disease Doctor", "Proctologist", "Vascular Surgeon", "Urologist"
]

FIRST_NAMES = ["Karthik", "Priya", "Arun", "Divya", "Suresh", "Ramesh", "Ananya", "Vikram", "Neha", "Rahul", "Aishwarya", "Balaji", "Nithya", "Manoj", "Sneha", "Ashok", "Kavya", "Prakash", "Swathi", "Vignesh"]
LAST_NAMES = ["Kumar", "Rajan", "Iyer", "Nair", "Krishnan", "Menon", "Reddy", "Rao", "Sharma", "Varma", "Pillai", "Chacko", "Babu", "Raman", "Natarajan"]
LANGUAGES = ["English", "Tamil", "Telugu", "Hindi", "Malayalam"]

def get_qual(spec):
    quals = ["MBBS, MD", "MBBS, MS", "MBBS, DNB"]
    if spec == "Cardiologist": return "MBBS, MD, DM Cardiology"
    if spec == "Neurologist": return "MBBS, MD, DM Neurology"
    if spec == "Neurosurgeon": return "MBBS, MS, MCh Neurosurgery"
    if spec == "Vascular Surgeon": return "MBBS, MS, MCh Vascular Surgery"
    if spec == "Orthopedic": return "MBBS, MS Orthopaedics"
    if spec == "Gastroenterologist": return "MBBS, MD, DM Gastroenterology"
    if spec == "Urologist": return "MBBS, MS, MCh Urology"
    if spec == "Dermatologist": return "MBBS, MD Dermatology"
    if spec == "Endocrinologist": return "MBBS, MD, DM Endocrinology"
    if spec == "Primary Care Provider": return "MBBS, MD General Medicine"
    return random.choice(quals)

doctors = []
doc_id_counter = 1

for hosp in HOSPITALS:
    hosp["specialists"] = []

# Generate 10 doctors for each specialty
for spec in SPECIALTIES:
    for _ in range(10):
        hosp = random.choice(HOSPITALS)
        if spec not in hosp["specialists"]:
            hosp["specialists"].append(spec)
            
        fname = random.choice(FIRST_NAMES)
        lname = random.choice(LAST_NAMES)
        
        doc = {
            "id": f"doc_{doc_id_counter:03d}",
            "name": f"Dr. {fname} {lname}",
            "specialist": spec,
            "hospital": hosp["name"],
            "rating": round(random.uniform(4.0, 5.0), 1),
            "experience_years": random.randint(5, 30),
            "qualification": get_qual(spec),
            "phone": f"+91-9{random.randint(100000000, 999999999)}",
            "hospital_phone": hosp["phone"],
            "lat": hosp["lat"],
            "lng": hosp["lng"],
            "city": hosp["city"],
            "address": hosp["address"],
            "available": True,
            "available_today": random.choice([True, True, False]),
            "consultation_fee": random.choice([500, 800, 1000, 1200, 1500]),
            "languages": random.sample(LANGUAGES, random.randint(2, 4)),
            "review_count": random.randint(50, 1000),
            "time_slots": random.sample(["10:00 AM", "11:30 AM", "1:00 PM", "3:00 PM", "5:30 PM", "7:00 PM"], random.randint(2, 4))
        }
        doctors.append(doc)
        doc_id_counter += 1

with open("database/doctors.json", "w", encoding="utf-8") as f:
    json.dump(doctors, f, indent=2)

with open("database/hospitals.json", "w", encoding="utf-8") as f:
    json.dump(HOSPITALS, f, indent=2)

print(f"Generated {len(doctors)} doctors and {len(HOSPITALS)} hospitals successfully.")
