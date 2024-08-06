n, b = tuple(map(int, input().split()))
arr = [int(input()) for _ in range(n)]

ans = 0

for i in range(n):
    tempSum = arr[i] / 2
    cnt = 0

    if tempSum > b:
        continue

    cnt = 1
    for j in range(n):
        if i == j:
            continue

        if tempSum + arr[j] > b :
            continue

        cnt += 1
        tempSum += arr[j]

    if tempSum > b :
        cnt -= 1
    
    ans = max(ans, cnt)

print(ans)