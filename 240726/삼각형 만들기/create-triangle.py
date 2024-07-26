n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = 0

for i in range(n - 2) :
    for j in range(i + 1, n - 1) :
        for k in range(j + 1, n) :

            if arr[i][0] == arr[j][0] :
                y = abs(arr[i][1] - arr[j][1])
                x = abs(arr[i][0] - arr[k][0])

            elif arr[i][0] == arr[k][0] :
                y = abs(arr[i][1] - arr[k][1])
                x = abs(arr[i][0] - arr[j][0])

            elif arr[j][0] == arr[k][0] :
                y = abs(arr[j][1] - arr[k][1])
                x = abs(arr[i][0] - arr[k][0])

            else :
                continue

            ans = max(ans, x * y)

print(ans)