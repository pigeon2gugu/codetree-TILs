x, y = tuple(map(int, input().split()))
ans = 0

for i in range(x, y + 1):
    temp = [0] * 10
    num_str = str(i)

    for digit in num_str:
        temp[int(digit)] += 1

    cnt = 0
    for count in temp:
        if count == 1:
            cnt += 1

    if cnt == 1:
        ans += 1

print(ans)