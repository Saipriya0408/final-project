import unittest
import os
import socket

# Check if browser is available or if selenium is installed
try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    SELENIUM_INSTALLED = True
except ImportError:
    SELENIUM_INSTALLED = False

def is_chrome_available():
    # Basic check for Chrome browser path presence on Windows/Linux
    if os.name == "nt":
        paths = [
            os.path.expandvars(r"%ProgramFiles%\Google\Chrome\Application\chrome.exe"),
            os.path.expandvars(r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"),
            os.path.expandvars(r"%LocalAppData%\Google\Chrome\Application\chrome.exe")
        ]
        return any(os.path.exists(p) for p in paths)
    else:
        # Linux/macOS
        return os.system("which google-chrome > /dev/null 2>&1") == 0 or os.system("which chromium-browser > /dev/null 2>&1") == 0

def is_server_running():
    try:
        with socket.create_connection(("127.0.0.1", 5000), timeout=1):
            return True
    except OSError:
        return False

class TestWebUI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not SELENIUM_INSTALLED:
            raise unittest.SkipTest("Not executed - environment dependency unavailable (selenium python library not installed)")
        if not is_chrome_available():
            raise unittest.SkipTest("Not executed - environment dependency unavailable (Chrome/Chromedriver not found on system)")
        if not is_server_running():
            raise unittest.SkipTest("Not executed - environment dependency unavailable (Flask backend server not running)")

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        try:
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.implicitly_wait(3)
        except Exception as e:
            raise unittest.SkipTest(f"Not executed - environment dependency unavailable (Failed to start ChromeDriver: {e})")

    def tearDown(self):
        if hasattr(self, "driver"):
            self.driver.quit()

    # 1. Onboarding Page Flow
    def test_onboarding_page(self):
        self.driver.get("http://localhost:5173/onboarding")
        self.assertIn("SymptoCare", self.driver.title or self.driver.page_source)

    # 2. Signup Page Flow
    def test_signup_page_elements(self):
        self.driver.get("http://localhost:5173/signup")
        fields = self.driver.find_elements(By.TAG_NAME, "input")
        self.assertGreaterEqual(len(fields), 3) # Name, Email, Phone, Password inputs

    # 3. Signin Page Flow
    def test_signin_page_elements(self):
        self.driver.get("http://localhost:5173/signin")
        email_or_phone = self.driver.find_element(By.ID, "email_or_phone")
        password = self.driver.find_element(By.ID, "password")
        self.assertIsNotNone(email_or_phone)
        self.assertIsNotNone(password)

    # 4. Symptoms Page Flow
    def test_symptoms_page(self):
        self.driver.get("http://localhost:5173/symptoms")
        page_content = self.driver.page_source
        self.assertTrue("symptom" in page_content.lower() or "analyze" in page_content.lower())

    # 5. Doctors Finder Page Flow
    def test_doctors_page(self):
        self.driver.get("http://localhost:5173/doctors")
        self.assertTrue("doctor" in self.driver.page_source.lower() or "specialist" in self.driver.page_source.lower())

    # 6. Hospitals Directory Page Flow
    def test_hospitals_page(self):
        self.driver.get("http://localhost:5173/hospitals")
        self.assertTrue("hospital" in self.driver.page_source.lower() or "department" in self.driver.page_source.lower())

    # 7. Recovery Plan Flow
    def test_recovery_plan_page(self):
        self.driver.get("http://localhost:5173/recovery-plan")
        self.assertTrue("plan" in self.driver.page_source.lower() or "recovery" in self.driver.page_source.lower())

    # 8. User Profile Dashboard Page Flow
    def test_profile_page(self):
        self.driver.get("http://localhost:5173/profile")
        self.assertTrue("profile" in self.driver.page_source.lower() or "history" in self.driver.page_source.lower())

if __name__ == "__main__":
    unittest.main()
