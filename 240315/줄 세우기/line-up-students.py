n = int(input())

class Student :
    def __init__(self, height, weight, number) :
        self.height = height
        self.weight = weight
        self.number = number


inputs = [tuple(input().split()) for _ in range(n)]
students = [Student(int(h), int(w), idx) for idx, (h, w) in enumerate(inputs, start = 1)]

students.sort(key = lambda x : (-x.height, -x.weight, x.number))

for s in students :
    print(f"{s.height} {s.weight} {s.number}")