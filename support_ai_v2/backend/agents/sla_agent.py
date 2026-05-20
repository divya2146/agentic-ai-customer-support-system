class SLAAgent:

    def assign_sla(self, priority):

        if priority == "High":
            return "2 Hours"

        return "24 Hours"