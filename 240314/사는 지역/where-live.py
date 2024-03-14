n = int(input())

class User :
    def __init__(self, name, address, city) :
        self.name = name
        self.address = address
        self.city = city

users = []
for _ in range(n) :
    a, b, c = tuple(input().split())
    users.append(User(a, b, c))


idx = 0
for i in range(len(users)) :
    if users[i].name > users[idx].name :
        idx = i

print(f"name {users[idx].name}")
print(f"addr {users[idx].address}")
print(f"city {users[idx].city}")