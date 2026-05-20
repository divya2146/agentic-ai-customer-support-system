# app/database/db.py

import sqlite3

DB_NAME = "support_system.db"


# -----------------------------------
# Create Tickets Table
# -----------------------------------
def create_table():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        issue TEXT,
        department TEXT,
        priority TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()


# -----------------------------------
# Insert New Ticket
# -----------------------------------
def insert_ticket(user_id, issue, department, priority, status):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO tickets (user_id, issue, department, priority, status)
    VALUES (?, ?, ?, ?, ?)
    """, (user_id, issue, department, priority, status))

    conn.commit()
    conn.close()


# -----------------------------------
# Get All Tickets
# -----------------------------------
def get_all_tickets():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT * FROM tickets")
    rows = cur.fetchall()

    conn.close()
    return rows


# -----------------------------------
# Count Total Tickets
# -----------------------------------
def count_tickets():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM tickets")
    count = cur.fetchone()[0]

    conn.close()
    return count


# -----------------------------------
# Count High Priority Tickets
# -----------------------------------
def count_high_priority():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM tickets WHERE priority = 'High'")
    count = cur.fetchone()[0]

    conn.close()
    return count


# -----------------------------------
# Run File Directly
# -----------------------------------
if __name__ == "__main__":
    create_table()
    print("Database and tickets table created successfully.")