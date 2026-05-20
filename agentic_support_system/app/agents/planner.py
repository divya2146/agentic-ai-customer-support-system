def planner_agent(query):
    query = query.lower()

    if "refund" in query or "payment" in query or "money" in query:
        return "billing"

    elif "error" in query or "issue" in query or "problem" in query or "login" in query:
        return "technical"

    elif "cancel" in query or "delete account" in query:
        return "account"

    else:
        return "general"


if __name__ == "__main__":
    print(planner_agent("refund issue"))
    print(planner_agent("login error"))
    print(planner_agent("cancel my account"))
    print(planner_agent("hello"))