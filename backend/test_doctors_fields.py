import urllib.request, json

BASE = "http://10.250.236.211:5000/api"

def get(path):
    with urllib.request.urlopen(BASE + path, timeout=10) as r:
        return json.loads(r.read())

# 1. Doctor list - card view fields
r = get("/doctors?specialist=cardiologist")
print(f"GET /doctors?specialist=cardiologist -> {r['data']['total']} results")
print()
for d in r["data"]["doctors"]:
    print(f"  Card: {d['name']} [{d['specialist']}]")
    print(f"    available      : {d['available']}")
    print(f"    available_today: {d['available_today']}")
    print(f"    rating         : {d['rating']} ({d['review_count']} reviews)")
    print(f"    experience     : {d['experience_years']} years")
    print(f"    fee            : Rs.{d['consultation_fee']}")
    print(f"    time_slots     : {d['time_slots']}")
    print()

# 2. Single doctor detail view
print("GET /doctors/doc_026 (Dr. Karthikeyan Subramanian - detail view)")
r = get("/doctors/doc_026")
d = r["data"]
print(f"  name          : {d['name']}")
print(f"  specialist    : {d['specialist']}")
print(f"  rating        : {d['rating']} ({d['review_count']} reviews)")
print(f"  available     : {d['available']}")
print(f"  experience    : {d['experience_years']} years")
print(f"  fee           : Rs.{d['consultation_fee']}")
print(f"  time_slots    : {d['time_slots']}")
print(f"  phone         : {d['phone']}")
print(f"  lat/lng       : {d['lat']}, {d['lng']}")
print(f"  qualification : {d['qualification']}")
print(f"  address       : {d['address']}")
print(f"  hospital      : {d['hospital']}")
