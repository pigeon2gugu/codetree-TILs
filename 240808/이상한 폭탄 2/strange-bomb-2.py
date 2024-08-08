n, k = tuple(map(int, input().split()))
bombs = [
    int(input())
    for _ in range(n)
]

ans = -1

for i in range(n) :
    for j in range(i+1, n) :
        if bombs[i] == bombs[j] and (j - i) <= k :
            ans = max(ans, bombs[i])


print(ans)