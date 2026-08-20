import urllib.request, json, sys

BASE = "http://10.250.236.211:5000/api"
passed = 0
failed = 0

def test(label, url, method="GET", data=None):
    global passed, failed
    req = urllib.request.Request(url, method=method)
    req.add_header("Content-Type", "application/json")
    if data:
        req.data = json.dumps(data).encode()
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            body = json.loads(r.read())
            print(f"[PASS] {label}")
            passed += 1
            return body
    except urllib.error.HTTPError as e:
        body = json.loads(e.read())
        print(f"[PASS] {label} (expected error: {body.get('error', {}).get('code')})")
        passed += 1
        return body
    except Exception as e:
        print(f"[FAIL] {label}: {e}")
        failed += 1
        return None

print("=" * 60)
print("  SymptoCare API Test Suite")
print("=" * 60)

# 1. Health check
r = test("Health Check", f"{BASE}/health")
if r:
    d = r["data"]
    print(f"       Model ready={d['modelReady']}, symptoms={d['knownSymptoms']}")

# 2. NLP - chest pain
r = test("NLP: chest pain + breathing", f"{BASE}/analyze-symptoms", "POST",
         {"message": "I have chest pain and breathing issues"})
if r and r.get("success"):
    d = r["data"]
    print(f"       symptoms={d['normalizedSymptoms']}")
    print(f"       disease={d['predictedDisease']} | specialist={d['recommendedSpecialist']} | conf={d['confidence']}")

# 3. NLP - informal language
r = test("NLP: informal bro language", f"{BASE}/analyze-symptoms", "POST",
         {"message": "bro my head hurts and I feel feverish"})
if r and r.get("success"):
    d = r["data"]
    print(f"       symptoms={d['normalizedSymptoms']}")
    print(f"       disease={d['predictedDisease']} | specialist={d['recommendedSpecialist']}")

# 4. NLP - another informal
r = test("NLP: tight chest cant breathe", f"{BASE}/analyze-symptoms", "POST",
         {"message": "my chest feels tight and I cant breathe"})
if r and r.get("success"):
    d = r["data"]
    print(f"       symptoms={d['normalizedSymptoms']}")

# 5. Icon-based
r = test("Icon: high_fever + cough + fatigue", f"{BASE}/analyze-symptoms", "POST",
         {"symptoms": ["high_fever", "cough", "fatigue"]})
if r and r.get("success"):
    d = r["data"]
    print(f"       disease={d['predictedDisease']} | specialist={d['recommendedSpecialist']}")

# 6. Icon - headache
r = test("Icon: headache + dizziness", f"{BASE}/analyze-symptoms", "POST",
         {"symptoms": ["headache", "dizziness", "nausea"]})
if r and r.get("success"):
    d = r["data"]
    print(f"       disease={d['predictedDisease']} | specialist={d['recommendedSpecialist']}")

# 7. Symptoms list
r = test("GET /api/symptoms", f"{BASE}/symptoms")
if r:
    print(f"       Total symptoms: {r['data']['total']}")

# 8. Doctor search
r = test("GET /api/doctors?specialist=cardiologist", f"{BASE}/doctors?specialist=cardiologist")
if r:
    docs = r["data"]["doctors"]
    print(f"       Found {r['data']['total']} cardiologists")
    if docs:
        print(f"       Top: {docs[0]['name']} @ {docs[0]['hospital']} (rating={docs[0]['rating']})")

# 9. Doctor search with lat/lng
r = test("GET /api/doctors with Bangalore coords", f"{BASE}/doctors?specialist=neurologist&lat=12.97&lng=77.59")
if r:
    docs = r["data"]["doctors"]
    print(f"       Found {r['data']['total']} neurologists near Bangalore")
    if docs:
        print(f"       Closest: {docs[0]['name']} ({docs[0].get('distance', '?')})")

# 10. Hospitals
r = test("GET /api/hospitals Bangalore", f"{BASE}/hospitals?lat=12.97&lng=77.59")
if r:
    print(f"       Found {r['data']['total']} hospitals near Bangalore")

# 11. Specialists
r = test("GET /api/specialists", f"{BASE}/specialists")
if r:
    print(f"       Categories: {r['data']['specialists']}")

# 12. Diseases
r = test("GET /api/diseases", f"{BASE}/diseases")
if r:
    print(f"       Total diseases: {r['data']['total']}")

# 13. Error: empty message
r = test("Error handling: empty message", f"{BASE}/analyze-symptoms", "POST", {"message": ""})
if r:
    print(f"       success={r['success']} (expected False)")

# 14. Error: bad body
r = test("Error handling: missing fields", f"{BASE}/analyze-symptoms", "POST", {"foo": "bar"})
if r:
    print(f"       success={r['success']} (expected False)")

print()
print("=" * 60)
print(f"  Results: {passed} passed, {failed} failed")
print("=" * 60)
