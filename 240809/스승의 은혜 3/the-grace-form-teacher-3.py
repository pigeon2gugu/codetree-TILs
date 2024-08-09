n, b = tuple(map(int, input().split()))

arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

arr.sort(key=lambda x: x[0])
ans = 0

for i in range(n) :
    price = arr[i][0] / 2 + arr[i][1]
    cnt = 1

    for j in range(n) :

        if i == j :
            continue

        if price > b :
            break

        cnt += 1
        price += (arr[j][0] + arr[j][1])

    
    if price > b :
        cnt -= 1

    ans = max(ans, cnt)

print(ans)