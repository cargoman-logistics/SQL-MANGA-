import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER,
    city TEXT
)
""")

employees = [
    (1, "Rahul", "IT", 50000, "Hyderabad"),
    (2, "Anjali", "HR", 40000, "Mumbai"),
    (3, "Sai", "IT", 60000, "Hyderabad"),
    (4, "Kiran", "Finance", 45000, "Chennai"),
    (5, "Priya", "IT", 70000, "Bangalore")
]

cursor.executemany(
    "INSERT OR REPLACE INTO employees VALUES (?, ?, ?, ?, ?)",
    employees
)

conn.commit()
conn.close()

print("Database created!")
