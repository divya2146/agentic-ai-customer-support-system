class EscalationAgent:

    def check_escalation(self, priority, sentiment):

        if priority == "High" or sentiment == "Negative":
            return "Yes"

        return "No"