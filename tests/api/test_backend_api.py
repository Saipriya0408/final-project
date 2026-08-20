import unittest
import urllib.request
import json
import socket

BASE_URL = "http://127.0.0.1:5000/api"

def is_server_running():
    try:
        with socket.create_connection(("127.0.0.1", 5000), timeout=1):
            return True
    except OSError:
        return False

class TestBackendAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not is_server_running():
            raise unittest.SkipTest("Flask API backend server is not running on localhost:5000")

    def make_request(self, path, method="GET", data=None):
        url = f"{BASE_URL}{path}"
        req = urllib.request.Request(url, method=method)
        req.add_header("Content-Type", "application/json")
        if data is not None:
            req.data = json.dumps(data).encode("utf-8")
        
        try:
            with urllib.request.urlopen(req, timeout=5) as response:
                status_code = response.status
                body = response.read().decode("utf-8")
                return status_code, json.loads(body)
        except urllib.error.HTTPError as e:
            status_code = e.code
            body = e.read().decode("utf-8")
            try:
                parsed_body = json.loads(body)
            except json.JSONDecodeError:
                parsed_body = {"raw": body}
            return status_code, parsed_body
        except Exception as e:
            return 500, {"error": str(e)}

    # 1. Health check tests
    def test_health_check_success(self):
        status, response = self.make_request("/health")
        self.assertEqual(status, 200)
        self.assertTrue(response.get("success"))
        self.assertEqual(response["data"]["status"], "ok")
        self.assertIn("modelReady", response["data"])

    # 2. Symptoms analysis tests
    def test_analyze_symptoms_nlp_success(self):
        payload = {"message": "I have chest pain and breathing issues"}
        status, response = self.make_request("/analyze-symptoms", "POST", payload)
        self.assertEqual(status, 200)
        self.assertTrue(response.get("success"))
        self.assertIn("predictedDisease", response["data"])
        self.assertIn("recommendedSpecialist", response["data"])

    def test_analyze_symptoms_icons_success(self):
        payload = {"symptoms": ["cough", "high_fever", "fatigue"]}
        status, response = self.make_request("/analyze-symptoms", "POST", payload)
        self.assertEqual(status, 200)
        self.assertTrue(response.get("success"))
        self.assertIn("predictedDisease", response["data"])

    def test_analyze_symptoms_empty_payload(self):
        status, response = self.make_request("/analyze-symptoms", "POST", {})
        self.assertEqual(status, 400)
        self.assertFalse(response.get("success"))
        self.assertEqual(response["error"]["code"], "VALIDATION_ERROR")

    def test_analyze_symptoms_empty_message(self):
        status, response = self.make_request("/analyze-symptoms", "POST", {"message": ""})
        self.assertEqual(status, 400)
        self.assertFalse(response.get("success"))

    # 3. Doctors endpoint tests
    def test_get_doctors_no_params(self):
        status, response = self.make_request("/doctors")
        self.assertEqual(status, 200)
        self.assertTrue(response.get("success"))
        self.assertGreaterEqual(response["data"]["total"], 0)

    def test_get_doctors_with_specialist(self):
        status, response = self.make_request("/doctors?specialist=cardiologist")
        self.assertEqual(status, 200)
        self.assertTrue(response.get("success"))
        for doc in response["data"]["doctors"]:
            self.assertEqual(doc["specialist"].lower(), "cardiologist")

    def test_get_doctors_with_coordinates(self):
        status, response = self.make_request("/doctors?specialist=neurologist&lat=13.08&lng=80.27")
        self.assertEqual(status, 200)
        self.assertTrue(response.get("success"))
        if response["data"]["doctors"]:
            self.assertIn("distance", response["data"]["doctors"][0])

    # 4. Hospitals endpoint tests
    def test_get_hospitals_coordinates(self):
        status, response = self.make_request("/hospitals?lat=13.08&lng=80.27")
        self.assertEqual(status, 200)
        self.assertTrue(response.get("success"))
        self.assertGreaterEqual(response["data"]["total"], 0)

    # 5. Authentication tests
    def test_auth_flow(self):
        # Create a unique email to prevent duplicate registration issues
        import time
        ts = int(time.time())
        email = f"test_{ts}@example.com"
        phone = f"99{ts % 100000000:08d}"
        
        signup_payload = {
            "name": "Integration Test User",
            "phone": phone,
            "email": email,
            "password": "password123"
        }
        
        # Signup Test
        status, response = self.make_request("/auth/signup", "POST", signup_payload)
        self.assertEqual(status, 201)
        self.assertTrue(response.get("success"))
        
        # Login Test (Valid Credentials)
        login_payload = {
            "email_or_phone": email,
            "password": "password123"
        }
        status, response = self.make_request("/auth/login", "POST", login_payload)
        self.assertEqual(status, 200)
        self.assertTrue(response.get("success"))
        self.assertIn("user", response["data"])
        
        # Login Test (Invalid Credentials)
        login_payload["password"] = "wrongpassword"
        status, response = self.make_request("/auth/login", "POST", login_payload)
        self.assertEqual(status, 401)
        self.assertFalse(response.get("success"))

if __name__ == "__main__":
    unittest.main()
