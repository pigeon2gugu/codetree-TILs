n = 5

class User :
    def __init__(self, name, height, weight) :
        self.name = name
        self.height = height
        self.weight = weight


inputs = [tuple(input().split()) for _ in range(n)]
users = [User(n, int(h), float(w)) for n, h, w in inputs]

users.sort(key = lambda x : x.name)

print("name")
for u in users :
    print(f"{u.name} {u.height} {u.weight:.1f}")
print()

users.sort(key = lambda x : -x.height)

print("height")
for u in users :
    print(f"{u.name} {u.height} {u.weight:.1f}")