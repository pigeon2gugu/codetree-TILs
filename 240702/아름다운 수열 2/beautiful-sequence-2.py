n, m = map(int, input().split())
arr = list(map(int, input().split()))
subArr = list(map(int, input().split()))
ans = 0

sortedSubArr = sorted(subArr)

for i in range(n - m + 1) :
    if sorted(arr[i:i+m]) == sortedSubArr:
        ans += 1


print(ans)