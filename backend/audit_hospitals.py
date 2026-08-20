import json

with open("database/hospitals.json") as f:
    hosps = json.load(f)

print(f"Total hospitals: {len(hosps)}")
print(f"All Chennai: {all(h['city'] == 'Chennai' for h in hosps)}")
print()

# Show all fields present in each record
required_ui_fields = ["id", "name", "rating", "review_count", "address",
                      "lat", "lng", "phone", "emergency_phone", "emergency",
                      "beds", "departments", "city"]

print("=== Field coverage check ===")
for field in required_ui_fields:
    covered = all(field in h for h in hosps)
    print(f"  {'OK' if covered else 'MISSING'} — {field}")

print()
print("=== All hospitals ===")
for h in hosps:
    depts = [d["name"] for d in h["departments"]]
    print(f"  [{h['id']}] {h['name']}")
    print(f"         Rating    : {h['rating']} ({h['review_count']} reviews)")
    print(f"         Beds      : {h['beds']}")
    print(f"         Emergency : {h['emergency']}")
    print(f"         Phone     : {h['phone']}")
    print(f"         Emrg Ph   : {h['emergency_phone']}")
    print(f"         Depts     : {', '.join(depts)}")
    print()
