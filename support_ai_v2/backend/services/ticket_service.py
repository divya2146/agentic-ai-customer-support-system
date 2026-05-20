from db import save_ticket, get_all_tickets
from agents.orchestrator import OrchestratorAgent


class TicketService:

    def __init__(self):
        self.orchestrator = OrchestratorAgent()

    def create_ticket(self, customer_name, issue):

        ai_result = self.orchestrator.process_ticket(issue)

        ticket_data = {
            "customer_name": customer_name,
            "issue": issue,
            "category": ai_result["category"],
            "priority": ai_result["priority"],
            "sentiment": ai_result["sentiment"],
            "department": ai_result["department"],
            "escalation": ai_result["escalation"],
            "resolution": ai_result["resolution"],
            "sla": ai_result["sla"]
        }

        ticket_id = save_ticket(ticket_data)

        ticket_data["id"] = ticket_id

        return ticket_data

    def get_tickets(self):

        return get_all_tickets()