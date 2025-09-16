import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

def insert(date, name, age, gender, ph_no, center, tests, address):
    age = int(age)
    ph_no = int(ph_no)

    cursor.execute("""
    INSERT INTO "patient_data" ("date", "name", "age", "gender", "ph_no", "center", "tests", "address")
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (date, name, age, gender, ph_no, center, tests, address))
    conn.commit()
    conn.close()