import sys

n = int(input())
rooms = [int(input()) for _ in range(n)]

minDisntance = sys.maxsize

for i in range(len(rooms)) :
    distance = 0
    for j in range(len(rooms)) :
        if j < i :
            distance += rooms[j] * (len(rooms) + (j - i))
        else :
            distance += rooms[j] * (j - i)

    minDisntance = min(distance, minDisntance)

print(minDisntance)