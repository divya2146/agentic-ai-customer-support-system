import sqlite3

DB_NAME = "../support_tickets.db"


def create_table():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT,
        issue TEXT,
        category TEXT,
        priority TEXT,
        sentiment TEXT,
        department TEXT,
        escalation TEXT,
        resolution TEXT,
        sla TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_ticket(ticket):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO tickets (
        customer_name,
        issue,
        category,
        priority,
        sentiment,
        department,
        escalation,
        resolution,
        sla
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        ticket["customer_name"],
        ticket["issue"],
        ticket["category"],
        ticket["priority"],
        ticket["sentiment"],
        ticket["department"],
        ticket["escalation"],
        ticket["resolution"],
        ticket["sla"]
    ))

    conn.commit()

    ticket_id = cursor.lastrowid

    conn.close()

    return ticket_id


def get_all_tickets():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tickets")

    rows = cursor.fetchall()

    conn.close()

    tickets = []

    for row in rows:

        tickets.append({
            "id": row[0],
            "customer_name": row[1],
            "issue": row[2],
            "category": row[3],
            "priority": row[4],
            "sentiment": row[5],
            "department": row[6],
            "escalation": row[7],
            "resolution": row[8],
            "sla": row[9]
        })

    return tickets


create_table()