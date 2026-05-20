from agents.classifier_agent import ClassifierAgent
from agents.priority_agent import PriorityAgent
from agents.sentiment_agent import SentimentAgent
from agents.routing_agent import RoutingAgent
from agents.escalation_agent import EscalationAgent
from agents.resolution_agent import ResolutionAgent
from agents.sla_agent import SLAAgent


class OrchestratorAgent:

    def process_ticket(self, issue):

        classifier = ClassifierAgent()
        priority_agent = PriorityAgent()
        sentiment_agent = SentimentAgent()
        routing_agent = RoutingAgent()
        escalation_agent = EscalationAgent()
        resolution_agent = ResolutionAgent()
        sla_agent = SLAAgent()

        category = classifier.classify_ticket(issue)

        priority = priority_agent.detect_priority(issue)

        sentiment = sentiment_agent.analyze_sentiment(issue)

        department = routing_agent.route_ticket(category)

        escalation = escalation_agent.check_escalation(
            priority,
            sentiment
        )

        resolution = resolution_agent.generate_resolution(category)

        sla = sla_agent.assign_sla(priority)

        return {
            "category": category,
            "priority": priority,
            "sentiment": sentiment,
            "department": department,
            "escalation": escalation,
            "resolution": resolution,
            "sla": sla
        }