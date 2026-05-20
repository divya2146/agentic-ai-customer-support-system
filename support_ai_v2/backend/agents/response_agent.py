class ResponseAgent:

    def generate_response(self, category):

        responses = {

            "Billing": "Billing team will contact you shortly.",

            "Refund": "Refund request is under process.",

            "Security": "Security team is investigating the issue.",

            "Logistics": "Delivery team is checking your shipment.",

            "General": "Support team will assist you soon."
        }

        return responses.get(
            category,
            "Support team will contact you."
        )