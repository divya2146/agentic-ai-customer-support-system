ticket_count = 1000

def create_ticket(issue_type, user_query):
    global ticket_count

    ticket_count += 1

    return {
        "ticket_id": ticket_count,
        "department": issue_type,
        "issue": user_query,
        "status": "Open"
    }


# test
if __name__ == "__main__":
    ticket = create_ticket("technical", "Unable to login")

    print(ticket)