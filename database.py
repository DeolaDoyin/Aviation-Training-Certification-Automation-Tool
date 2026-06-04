import sqlite3

conn = sqlite3.connect("aviation_certifications.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS personnel (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS certifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    personnel_id INTEGER,
    certification_name TEXT,
    issue_date TEXT,
    validity_years INTEGER,
    FOREIGN KEY(personnel_id) REFERENCES personnel(id)
)
""")

conn.commit()
conn.close()

print("Database created successfully.")
