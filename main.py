from collections import defaultdict, deque


def check_relation(net: tuple, person_name: str, friend_name: str) -> bool:
    graph = defaultdict(set)
    for user1, user2 in net:
        graph[user1].add(user2)
        graph[user2].add(user1)
    queue = deque([person_name])
    visited = {person_name}
    while queue:
        current_user = queue.popleft()
        if current_user == friend_name:
            return True
        for friend in graph[current_user]:
            if friend not in visited:
                visited.add(friend)
                queue.append(friend)
    return False


if __name__ == '__main__':
    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша")
    )
    print(check_relation(net,'Дима','Настя'))
