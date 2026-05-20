class AnalyticsAgent:

    def generate_analytics(self, tickets):

        total = len(tickets)

        high_priority = 0

        for ticket in tickets:
            if ticket["priority"] == "High":
                high_priority += 1

        return {
            "total_tickets": total,
            "high_priority_tickets": high_priority
        }