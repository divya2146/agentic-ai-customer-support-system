# backend/agents/department_agent.py

def assign_department(category: str):

    mapping = {
        "Payment": "Finance Team",
        "Authentication": "Auth Team",
        "Technical": "Engineering Team",
        "Security": "Cyber Security Team",
        "General": "Customer Support Team"
    }

    return mapping.get(category, "Support Team")