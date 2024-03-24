n, k = tuple(map(int, input().split()))
blocks = [0 for _ in range(n)]

for _ in range(k) :
    start, end = tuple(map(int, input().split()))
    for i in range(start-1, end) :
        blocks[i] += 1

print(max(blocks))