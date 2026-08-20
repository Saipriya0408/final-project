import unittest
import json
from app import app
from database import get_db_connection

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        
        # Clear users table before testing
        conn = get_db_connection()
        conn.execute("DELETE FROM users")
        conn.commit()
        conn.close()

    def test_registration_valid(self):
        payload = {
            "name": "Test User",
            "phone": "1234567890",
            "email": "test@example.com",
            "password": "password123"
        }
        res = self.app.post('/api/auth/signup', json=payload)
        print("Registration Valid Test:")
        print("Status Code:", res.status_code)
        print("Response:", res.get_json())
        
    def test_registration_duplicate_email(self):
        payload = {
            "name": "Test User",
            "phone": "1234567890",
            "email": "test@example.com",
            "password": "password123"
        }
        self.app.post('/api/auth/signup', json=payload)
        
        # Try duplicate email with different phone
        payload2 = {
            "name": "Test User 2",
            "phone": "0987654321",
            "email": "test@example.com",
            "password": "password123"
        }
        res = self.app.post('/api/auth/signup', json=payload2)
        print("Registration Duplicate Test:")
        print("Status Code:", res.status_code)
        print("Response:", res.get_json())
        
    def test_login_valid(self):
        payload = {
            "name": "Test User",
            "phone": "1234567890",
            "email": "test@example.com",
            "password": "password123"
        }
        self.app.post('/api/auth/signup', json=payload)
        
        login_payload = {
            "email_or_phone": "test@example.com",
            "password": "password123"
        }
        res = self.app.post('/api/auth/login', json=login_payload)
        print("Login Valid Test:")
        print("Status Code:", res.status_code)
        print("Response:", res.get_json())
        
    def test_login_invalid_password(self):
        payload = {
            "name": "Test User",
            "phone": "1234567890",
            "email": "test@example.com",
            "password": "password123"
        }
        self.app.post('/api/auth/signup', json=payload)
        
        login_payload = {
            "email_or_phone": "test@example.com",
            "password": "wrongpassword"
        }
        res = self.app.post('/api/auth/login', json=login_payload)
        print("Login Invalid Password Test:")
        print("Status Code:", res.status_code)
        print("Response:", res.get_json())

if __name__ == '__main__':
    # run tests manually to see output
    tester = AuthTestCase()
    tester.setUp()
    tester.test_registration_valid()
    
    tester.setUp()
    tester.test_registration_duplicate_email()
    
    tester.setUp()
    tester.test_login_valid()
    
    tester.setUp()
    tester.test_login_invalid_password()
