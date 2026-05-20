import sqlite3

print("🔄 Starting DB merge...")

# OLD DATABASE (source)
old_db_path = "support_ai_v2/backend/tickets.db"

# NEW DATABASE (target)
new_db_path = "data/tickets.db"

# connect to old DB
old_conn = sqlite3.connect(old_db_path)
old_cursor = old_conn.cursor()

# connect to new DB
new_conn = sqlite3.connect(new_db_path)
new_cursor = new_conn.cursor()

# fetch old tickets
old_cursor.execute("SELECT * FROM tickets")
rows = old_cursor.fetchall()

print(f"📦 Found {len(rows)} old tickets")

merged_count = 0

for row in rows:
    try:
        # skipping ticket_id (row[0]) to avoid conflicts
        new_cursor.execute("""
            INSERT INTO tickets 
            (user_id, issue, response, escalation, priority, department, status, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, row[1:])

        merged_count += 1

    except Exception as e:
        print(f"⚠️ Skipped one row: {e}")

# save changes
new_conn.commit()

print(f"✅ Successfully merged {merged_count} tickets!")

# close connections
old_conn.close()
new_conn.close()

print("🎉 Merge completed!")