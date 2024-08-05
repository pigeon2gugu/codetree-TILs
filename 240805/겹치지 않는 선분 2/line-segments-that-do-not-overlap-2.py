n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n):

    isDuplicated = False

    for j in range(n):
        x11, x12 = arr[i]
        x21, x22 = arr[j]

        if (x11 - x21) * (x12 - x22) < 0 :
            isDuplicated = True

    if (isDuplicated == False) :
        ans += 1

print(ans)