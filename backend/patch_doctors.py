"""
Patch doctors.json to add UI-required fields:
  - review_count     : shown as "(248)" next to rating on card + detail
  - available_today  : drives the "Available Today" label on card
  - time_slots       : the booking slot chips ["10:00 AM", "2:00 PM", "4:30 PM"]
"""

import json, random

random.seed(42)   # reproducible

# Slot pools by time-of-day preference
MORNING   = ["9:00 AM", "9:30 AM", "10:00 AM", "10:30 AM", "11:00 AM", "11:30 AM"]
AFTERNOON = ["12:00 PM", "1:00 PM", "2:00 PM", "2:30 PM", "3:00 PM", "3:30 PM"]
EVENING   = ["4:00 PM", "4:30 PM", "5:00 PM", "5:30 PM", "6:00 PM"]

def pick_slots():
    """Return 3 realistic time slots spread across morning/afternoon/evening."""
    return [
        random.choice(MORNING),
        random.choice(AFTERNOON),
        random.choice(EVENING),
    ]

with open("database/doctors.json") as f:
    doctors = json.load(f)

for doc in doctors:
    # review_count: scale roughly with experience and rating
    base   = doc["experience_years"] * 40
    spread = random.randint(-80, 120)
    doc["review_count"]    = max(80, base + spread)

    # available_today: 80% of doctors available today
    doc["available_today"] = random.random() < 0.80

    # time_slots: 3 slots; fewer if not available today
    if doc["available_today"]:
        doc["time_slots"] = pick_slots()
    else:
        doc["time_slots"] = []

with open("database/doctors.json", "w") as f:
    json.dump(doctors, f, indent=2)

print(f"Patched {len(doctors)} doctors.")
print()
for doc in doctors[:5]:          # preview first 5
    print(f"  {doc['name']}")
    print(f"    review_count   : {doc['review_count']}")
    print(f"    available_today: {doc['available_today']}")
    print(f"    time_slots     : {doc['time_slots']}")
    print()
