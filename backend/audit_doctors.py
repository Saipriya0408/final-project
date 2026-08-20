import json

with open("database/doctors.json") as f:
    docs = json.load(f)

# Fields the UI needs based on screenshots
required = [
    "id", "name", "specialist", "hospital",
    "available",         # green "Available" badge
    "available_today",   # "Available Today" label
    "rating",            # star rating number
    "review_count",      # "(248)"
    "experience_years",  # "15 years"
    "consultation_fee",  # "₹800"
    "time_slots",        # ["10:00 AM", "2:00 PM", "4:30 PM"]
    "phone",             # Call button
    "lat", "lng",        # Navigate button + distance calc
    "qualification",     # About section
    "address",           # About section
    "languages",
]

print("=== Field coverage across all 36 doctors ===")
for field in required:
    ok = all(field in d for d in docs)
    print(f"  {'OK' if ok else 'MISSING'} — {field}")

print()
print("=== Chennai doctors — full UI field preview ===")
chennai_docs = [d for d in docs if d["city"] == "Chennai"]
for d in chennai_docs:
    print(f"  {d['name']} ({d['specialist']})")
    print(f"    Available      : {d['available']}  |  Available Today: {d['available_today']}")
    print(f"    Rating         : {d['rating']} ({d['review_count']} reviews)")
    print(f"    Experience     : {d['experience_years']} years")
    print(f"    Fee            : ₹{d['consultation_fee']}")
    print(f"    Time Slots     : {d['time_slots']}")
    print(f"    Phone          : {d['phone']}")
    print(f"    Hospital       : {d['hospital']}")
    print(f"    Address        : {d['address']}")
    print(f"    Qualification  : {d['qualification']}")
    print()
