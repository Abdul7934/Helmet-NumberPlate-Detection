import sqlite3

def connect_db():
    conn = sqlite3.connect('vehicle_data.db')
    return conn

def save_vehicle_data(license_plate, owner_info):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO vehicles (license_plate, owner_info) VALUES (?, ?)", (license_plate, owner_info))
    conn.commit()
    conn.close()
