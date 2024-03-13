id, level = tuple(input().split())

class User:
    def __init__(self, id, level) :
        self.id = id
        self.level = level


a = User("codetree", "10")
b = User(id, level)

print("user " + a.id + " lv " + a.level)
print("user " + b.id + " lv " + b.level)