class PriorityAgent:

    def detect_priority(self, issue):

        issue = issue.lower()

        high_keywords = [
            "hack",
            "hacked",
            "security",
            "urgent",
            "failed",
            "error"
        ]

        for word in high_keywords:
            if word in issue:
                return "High"

        return "Low"