import json

def search_knowledge(query):
    with open("data/knowledge.json", "r") as file:
        data = json.load(file)

    query = query.lower()

    for item in data:
        if query in item["question"].lower():
            return item["answer"]

    return "Sorry, no relevant answer found."


# test
if __name__ == "__main__":
    print(search_knowledge("refund"))
    print(search_knowledge("password"))
    print(search_knowledge("cancel"))