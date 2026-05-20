class ResolutionAgent:

    def generate_resolution(self, category):

        responses = {
            "Billing": "Finance team will contact you shortly.",
            "Security": "Security team is investigating the issue.",
            "Technical": "Technical support is resolving the issue.",
            "General": "Customer support will contact you soon."
        }

        return responses.get(category)