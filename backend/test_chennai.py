import urllib.request, json

BASE = "http://10.250.236.211:5000/api"

def get(path):
    with urllib.request.urlopen(BASE + path, timeout=10) as r:
        return json.loads(r.read())

# 1. Default call (no city, no lat/lng) — should return Chennai doctors only
r = get("/doctors?specialist=cardiologist")
print("=== Default /api/doctors?specialist=cardiologist (no city param) ===")
print(f"Count : {r['data']['total']}")
for d in r["data"]["doctors"]:
    print(f"  {d['name']} | {d['hospital']} | {d['city']}")

print()

# 2. All Chennai doctors — no specialist filter
r = get("/doctors")
print("=== Default /api/doctors (no filters) — should be Chennai only ===")
print(f"Count : {r['data']['total']}")
for d in r["data"]["doctors"]:
    print(f"  {d['name']:35s} | {d['specialist']:30s} | {d['city']}")

print()

# 3. Explicitly ask for a different city — should override default
r = get("/doctors?city=bangalore&specialist=cardiologist")
print("=== /api/doctors?city=bangalore&specialist=cardiologist (override) ===")
print(f"Count : {r['data']['total']}")
for d in r["data"]["doctors"]:
    print(f"  {d['name']} | {d['city']}")

print()

# 4. Hospitals default
r = get("/hospitals")
print("=== Default /api/hospitals (no filters) — should be Chennai only ===")
print(f"Count : {r['data']['total']}")
for h in r["data"]["hospitals"]:
    print(f"  {h['name']} | {h['city']}")
