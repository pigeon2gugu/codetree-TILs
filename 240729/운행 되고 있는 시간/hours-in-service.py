n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
ans = 0

for i in range(n):
    timeCount = [0] * 1001

    for j in range(n):
        if i == j:
            continue
    
        t1, t2 = arr[j]

        for k in range(t1, t2):
            timeCount[k] = 1

    ans = max(ans, sum(timeCount))

print(ans)