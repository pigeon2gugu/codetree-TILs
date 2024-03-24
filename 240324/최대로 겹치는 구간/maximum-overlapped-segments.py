n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
points = [0 for _ in range(min(segments, key=lambda x: x[0])[0], max(segments, key=lambda x: x[1])[1]+1)]

for s in segments :
    for i in range(s[0], s[1]) :
        points[i] += 1


print(max(points))