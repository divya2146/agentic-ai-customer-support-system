class RoutingAgent:

    def route_ticket(self, category):

        routes = {
            "Billing": "Finance Team",
            "Security": "Cyber Security Team",
            "Technical": "Tech Support Team",
            "General": "Customer Support"
        }

        return routes.get(category, "Customer Support")