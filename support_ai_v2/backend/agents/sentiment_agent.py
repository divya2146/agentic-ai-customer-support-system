class SentimentAgent:

    def analyze_sentiment(self, issue):

        issue = issue.lower()

        negative_words = [
            "angry",
            "bad",
            "worst",
            "failed",
            "error"
        ]

        for word in negative_words:
            if word in issue:
                return "Negative"

        return "Neutral"