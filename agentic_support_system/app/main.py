# app/main.py

from app.agents.priority import detect_priority
from app.tools.ticket_tool import create_ticket
from app.database.db import create_table, insert_ticket


def run_support_agent(user_id, user_query):
    # Detect priority
    priority = detect_priority(user_query)

    # Create ticket (FIXED: pass user_query also)
    ticket = create_ticket(priority, user_query)

    # Extract values
    ticket_id = ticket["ticket_id"]
    department = ticket["department"]
    status = ticket["status"]

    # Save to database
    insert_ticket(
        user_id=user_id,
        issue=user_query,
        department=department,
        priority=priority,
        status=status
    )

    # Final reply
    response = f"""
Ticket ID   : {ticket_id}
Issue       : {user_query}
Department  : {department}
Priority    : {priority}
Status      : {status}

Your request has been registered successfully.
Our team will contact you soon.
"""
    return response


# -----------------------------
# Main Program
# -----------------------------
if __name__ == "__main__":
    create_table()

    print("🚀 AI Customer Support System Started")

    while True:
        user_query = input("\nEnter your issue (type 'exit' to quit): ").strip()

        if user_query.lower() == "exit":
            print("Goodbye!")
            break

        if user_query == "":
            print("Please enter an issue.")
            continue

        result = run_support_agent("user1", user_query)

        print("\nAI Support Reply:")
        print(result)
        print("-" * 50)