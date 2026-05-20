def detect_priority(query):
    query = query.lower()

    high_keywords = [
        "payment failed",
        "charged twice",
        "hacked",
        "fraud",
        "refund urgent",
        "account locked",
        "cannot access account",
        "security issue",
        "server down",
        "critical",
        "urgent"
    ]

    medium_keywords = [
        "login issue",
        "refund",
        "slow",
        "error",
        "problem",
        "failed",
        "not working",
        "unable to login",
        "password reset"
    ]

    for word in high_keywords:
        if word in query:
            return "High"

    for word in medium_keywords:
        if word in query:
            return "Medium"

    return "Low"


if __name__ == "__main__":
    print("🚨 Priority Detection System Started")

    while True:
        issue = input("\nEnter issue (type 'exit' to quit): ").strip()

        if issue.lower() == "exit":
            print("Goodbye!")
            break

        if issue == "":
            print("Please enter an issue.")
            continue

        priority = detect_priority(issue)
        print("Detected Priority:", priority)