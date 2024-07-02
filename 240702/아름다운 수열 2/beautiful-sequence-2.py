n, m = map(int, input().split())
arr = list(map(int, input().split()))
subArr = list(map(int, input().split()))
ans = 0

for i in range(n - m + 1) :
    cnt = 0
    for j in range(i, i + m) :
        for k in range(m) :
            if arr[j] == subArr[k] :
                cnt += 1

    if cnt >= m :
        ans += 1


print(ans)