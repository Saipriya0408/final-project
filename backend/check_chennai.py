import json

with open("database/doctors.json") as f:
    docs = json.load(f)

chennai = [d for d in docs if d["city"].lower() == "chennai"]
print(f"Total doctors in database : {len(docs)}")
print(f"Chennai doctors           : {len(chennai)}")
print()

for d in chennai:
    print(f"  ID         : {d['id']}")
    print(f"  Name       : {d['name']}")
    print(f"  Specialist : {d['specialist']}")
    print(f"  Hospital   : {d['hospital']}")
    print(f"  Phone      : {d['phone']}")
    print(f"  Rating     : {d['rating']}")
    print(f"  Lat/Lng    : {d['lat']}, {d['lng']}")
    print()

all_specs     = sorted(set(d["specialist"] for d in docs))
chennai_specs = sorted(set(d["specialist"] for d in chennai))
missing       = [s for s in all_specs if s not in chennai_specs]

print("Specialists already covered in Chennai:")
for s in chennai_specs:
    print(f"  + {s}")
print()
print("Specialists NOT yet in Chennai (need to add):")
for s in missing:
    print(f"  - {s}")
