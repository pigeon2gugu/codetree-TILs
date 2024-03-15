n = int(input())

class Student :
    def __init__(self, name, a, b, c) :
        self.name = name
        self.a = a
        self.b = b
        self.c = c


inputs = [tuple(input().split()) for _ in range(n)]
students = [Student(name, int(a), int(b), int(c)) for name, a, b, c in inputs]

students.sort(key = lambda x : x.a + x.b + x.c)

for s in students :
    print(f"{s.name} {s.a} {s.b} {s.c}")