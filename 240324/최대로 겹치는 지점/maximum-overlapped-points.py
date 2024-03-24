n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

points = [0] * (max(segments, key = lambda x : x[1])[1] + 1)

for s, e in segments :
    for i in range(s, e+1) :
        points[i] += 1

print(max(points))