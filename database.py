import sqlite3
from datetime import datetime

def init_db():
    """Initialize the database and create members table"""
    conn = sqlite3.connect('church_members.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone TEXT,
        date_of_birth DATE NOT NULL,
        gender TEXT NOT NULL,
        address TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT NOT NULL,
        postal_code TEXT NOT NULL,
        marital_status TEXT NOT NULL,
        occupation TEXT,
        emergency_contact_name TEXT NOT NULL,
        emergency_contact_phone TEXT NOT NULL,
        spiritual_status TEXT NOT NULL,
        baptism_date DATE,
        previous_church TEXT,
        skills_interests TEXT,
        join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    conn.commit()
    conn.close()

def add_member(member_data):
    """Add a new member to the database"""
    conn = sqlite3.connect('church_members.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        INSERT INTO members (
            first_name, last_name, email, phone, date_of_birth,
            gender, address, city, state, postal_code,
            marital_status, occupation, emergency_contact_name,
            emergency_contact_phone, spiritual_status, baptism_date,
            previous_church, skills_interests
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            member_data['first_name'],
            member_data['last_name'],
            member_data['email'],
            member_data['phone'],
            member_data['date_of_birth'],
            member_data['gender'],
            member_data['address'],
            member_data['city'],
            member_data['state'],
            member_data['postal_code'],
            member_data['marital_status'],
            member_data['occupation'],
            member_data['emergency_contact_name'],
            member_data['emergency_contact_phone'],
            member_data['spiritual_status'],
            member_data['baptism_date'],
            member_data['previous_church'],
            member_data['skills_interests']
        ))
        
        conn.commit()
        member_id = cursor.lastrowid
        return member_id
    except sqlite3.IntegrityError as e:
        raise Exception(f"Email already exists: {e}")
    finally:
        conn.close()

def get_all_members():
    """Retrieve all members from the database"""
    conn = sqlite3.connect('church_members.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT * FROM members ORDER BY join_date DESC
    ''')
    
    members = cursor.fetchall()
    conn.close()
    
    return members

def get_member_count():
    """Get total number of members"""
    conn = sqlite3.connect('church_members.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM members')
    count = cursor.fetchone()[0]
    
    conn.close()
    return count

# Initialize the database when this module is imported
init_db()