import sqlite3
from database import get_db_connection

def register_user(name, phone, email, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Check if user already exists
        cursor.execute("SELECT id FROM users WHERE email = ? OR phone = ?", (email, phone))
        if cursor.fetchone():
            return None, "User with this email or phone already exists."

        # Insert new user
        # INSECURE FOR DEMO: In production, use werkzeug.security.generate_password_hash
        cursor.execute(
            "INSERT INTO users (name, phone, email, password) VALUES (?, ?, ?, ?)",
            (name, phone, email, password)
        )
        conn.commit()
        
        user_id = cursor.lastrowid
        
        safe_user = {
            "id": user_id,
            "name": name,
            "phone": phone,
            "email": email
        }
        return safe_user, None
        
    except sqlite3.IntegrityError:
        return None, "Database error: Could not register user."
    finally:
        conn.close()

def authenticate_user(email_or_phone, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "SELECT * FROM users WHERE email = ? OR phone = ?", 
            (email_or_phone, email_or_phone)
        )
        row = cursor.fetchone()
        
        if not row:
            return None, "User not found."
            
        # row is sqlite3.Row, act like a dict
        if row["password"] == password:
            safe_user = {
                "id": row["id"],
                "name": row["name"],
                "phone": row["phone"],
                "email": row["email"]
            }
            return safe_user, None
        else:
            return None, "Invalid password."
            
    finally:
        conn.close()

