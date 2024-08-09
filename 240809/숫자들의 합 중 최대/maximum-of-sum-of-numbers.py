x, y = tuple(map(int, input().split()))
ans = 0

for i in range(x, y + 1) :
    arr = list(map(int, str(i)))
    ans = max(ans, sum(arr))

print(ans)