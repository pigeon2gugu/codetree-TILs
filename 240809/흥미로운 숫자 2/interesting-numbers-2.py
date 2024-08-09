x, y = tuple(map(int, input().split()))
ans = 0

for i in range(x, y + 1) :
    cnt = 0
    setStr = set(list(str(i)))

    if len(setStr) == 2 :
        ans += 1

print(ans)