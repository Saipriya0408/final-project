import unittest
import urllib.request
import json
import socket

# Check if Appium Python client is installed
try:
    from appium import webdriver
    from appium.webdriver.common.appiumby import AppiumBy
    APPIUM_INSTALLED = True
except ImportError:
    APPIUM_INSTALLED = False

def is_appium_server_running():
    try:
        # Appium usually listens on 4723
        with socket.create_connection(("127.0.0.1", 4723), timeout=1):
            return True
    except OSError:
        return False

class TestAndroidAppium(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not APPIUM_INSTALLED:
            raise unittest.SkipTest("Not executed - environment dependency unavailable (appium-python-client library not installed)")
        if not is_appium_server_running():
            raise unittest.SkipTest("Not executed - environment dependency unavailable (Appium server not running on port 4723)")

    def setUp(self):
        desired_caps = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "deviceName": "Android Emulator",
            "appPackage": "com.simats.symptocareappfrontend",
            "appActivity": ".LoginActivity",
            "noReset": True
        }
        try:
            self.driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
            self.driver.implicitly_wait(5)
        except Exception as e:
            raise unittest.SkipTest(f"Not executed - environment dependency unavailable (Failed to connect to Appium driver: {e})")

    def tearDown(self):
        if hasattr(self, "driver"):
            self.driver.quit()

    # 1. App Launch Flow
    def test_app_launch(self):
        # Verify app launches by checking LoginActivity package
        self.assertEqual(self.driver.current_package, "com.simats.symptocareappfrontend")

    # 2. Login Flow
    def test_login_flow(self):
        # Locate username and password text inputs
        email_field = self.driver.find_element(AppiumBy.ID, "com.simats.symptocareappfrontend:id/login_email")
        password_field = self.driver.find_element(AppiumBy.ID, "com.simats.symptocareappfrontend:id/login_password")
        login_btn = self.driver.find_element(AppiumBy.ID, "com.simats.symptocareappfrontend:id/login_btn")
        
        email_field.send_keys("test@example.com")
        password_field.send_keys("password123")
        login_btn.click()
        
        # Verify transition to main screen
        self.assertIsNotNone(self.driver.find_element(AppiumBy.ID, "com.simats.symptocareappfrontend:id/home_layout"))

    # 3. Location Permission Check
    def test_location_permission(self):
        # Test app requests and checks for location permissions (Nearby Doctors/Hospitals)
        doctors_tab = self.driver.find_element(AppiumBy.ID, "com.simats.symptocareappfrontend:id/nav_doctors")
        doctors_tab.click()
        
        # Look for Android default permission request dialog
        permission_dialog = self.driver.find_elements(AppiumBy.ID, "com.android.permissioncontroller:id/permission_message")
        if permission_dialog:
            allow_btn = self.driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
            allow_btn.click()

    # 4. Symptoms Analysis Check
    def test_symptom_analysis_app(self):
        # Select symptoms in UI list and analyze
        symptoms_menu = self.driver.find_element(AppiumBy.ID, "com.simats.symptocareappfrontend:id/nav_symptoms")
        symptoms_menu.click()
        
        # Tap on symptom item list checkbox
        fever_checkbox = self.driver.find_element(AppiumBy.XPATH, "//*[@text='Fever']")
        fever_checkbox.click()
        
        analyze_btn = self.driver.find_element(AppiumBy.ID, "com.simats.symptocareappfrontend:id/btn_analyze")
        analyze_btn.click()
        
        # Verify transition to recovery dashboard
        disease_title = self.driver.find_element(AppiumBy.ID, "com.simats.symptocareappfrontend:id/disease_title")
        self.assertTrue("predicted" in disease_title.text.lower() or len(disease_title.text) > 0)

if __name__ == "__main__":
    unittest.main()
