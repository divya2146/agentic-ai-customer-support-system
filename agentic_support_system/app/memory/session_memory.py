memory = {}

def save_memory(user_id, message):
    if user_id not in memory:
        memory[user_id] = []

    memory[user_id].append(message)


def get_memory(user_id):
    return memory.get(user_id, [])


if __name__ == "__main__":
    save_memory("user1", "Hello")
    save_memory("user1", "Need refund")

    print(get_memory("user1"))