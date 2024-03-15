n = int(input())

class Point :
    def __init__(self, x, y, number) :
        self.x = x
        self.y = y
        self.number = number


inputs = [tuple(input().split()) for _ in range(n)]
points = [Point(int(x), int(y), idx) for idx, (x, y) in enumerate(inputs, start = 1)]

points.sort(key = lambda p : abs(p.x) + abs(p.y))

for p in points :
    print(p.number)