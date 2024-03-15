n = int(input())

class User :
    def __init__(self, name, height, weight) :
        self.name = name
        self.height = height
        self.weight = weight


inputs = [input().split() for _ in range(n)]
users = [User(a, int(b), int(c)) for a, b, c in inputs]

users.sort(key = lambda x : x.height)

for user in users :
    print(f"{user.name} {user.height} {user.weight}")