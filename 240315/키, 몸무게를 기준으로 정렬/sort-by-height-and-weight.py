n = int(input())

class User :
    def __init__(self, name, h, w) :
        self.name = name
        self.height = h
        self.weight = w


inputs = [tuple(input().split()) for _ in range(n)]
users = [User(n, int(h), int(w)) for (n, h, w) in inputs]

users.sort(key = lambda x : (x.height, -x.weight))

for u in users :
    print(u.name, u.height, u.weight)