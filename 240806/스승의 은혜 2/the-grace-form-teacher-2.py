n, b = tuple(map(int, input().split()))
arr = [int(input()) for _ in range(n)]

ans = 0

for i in range(n) :

    tempSum = arr[i] / 2
    cnt = 0

    for j in range(n) :

        if i == j :
            continue

        if tempSum > b :
            ans = max(ans, cnt)
            break
        
        cnt += 1
        tempSum += arr[j]

    
    ans = max(ans, cnt)


print(ans)