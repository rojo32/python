users = [{"id": 0, "name": "Hero"}, {"id": 1, "name": "Dunn"}, {"id": 2, "name": "arg"}]
friendship_pairs = [(0, 1), (0, 2), (1, 2)]

friendships = {user["id"]: [] for user in users}
for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

print(friendships)