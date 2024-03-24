maxL = 100 * 10 * 2

n = int(input())
movings = [(int(move[0]), move[1]) for move in [input().split() for _ in range(n)]]

points = [0] * (maxL + 1)

start = 1000
for m in movings:
    if m[1] == "L":
        for i in range(start - m[0], start):
            points[i] += 1
        start -= m[0]

    elif m[1] == "R":
        for i in range(start, start + m[0]):
            points[i] += 1
        start += m[0]

print(sum(1 for point in points if point >= 2))