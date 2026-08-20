import urllib.request, json, time

BASE = "http://10.250.236.211:5000/api"

def get(path):
    with urllib.request.urlopen(BASE + path, timeout=10) as r:
        return json.loads(r.read())

# Wait for server
time.sleep(3)

# 1. Default hospitals (no params) — should all be Chennai
r = get("/hospitals")
print(f"GET /api/hospitals (default) -> {r['data']['total']} hospitals")
for h in r["data"]["hospitals"]:
    dept_names = [d["name"] for d in h["departments"]]
    print(f"  {h['name']}")
    print(f"    rating: {h['rating']} ({h['review_count']} reviews)")
    print(f"    emergency: {h['emergency']}")
    print(f"    phone: {h['phone']}")
    print(f"    departments: {', '.join(dept_names[:4])} ...")
    print()

# 2. Single hospital detail (what the detail screen shows)
print("GET /api/hospitals/hosp_001 (detail view)")
r = get("/hospitals/hosp_001")
h = r["data"]
print(f"  Name        : {h['name']}")
print(f"  Rating      : {h['rating']} ({h['review_count']} reviews)")
print(f"  Address     : {h['address']}")
print(f"  Phone       : {h['phone']}")
print(f"  Emrg Phone  : {h['emergency_phone']}")
print(f"  Emergency   : {h['emergency']}")
print(f"  Beds        : {h['beds']}")
print(f"  Lat/Lng     : {h['lat']}, {h['lng']}")
print(f"  Departments :")
for d in h["departments"]:
    print(f"    - {d['name']} : {'Available' if d['available'] else 'Unavailable'}")
