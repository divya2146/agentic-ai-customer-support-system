class ClassifierAgent:

    def classify_ticket(self, issue):

        issue = issue.lower()

        if "payment" in issue or "refund" in issue:
            return "Billing"

        elif "hack" in issue or "security" in issue:
            return "Security"

        elif "bug" in issue or "error" in issue:
            return "Technical"

        return "General"