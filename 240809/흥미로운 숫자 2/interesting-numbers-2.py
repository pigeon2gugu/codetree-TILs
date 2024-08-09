x, y = tuple(map(int, input().split()))
ans = 0

for i in range(x, y + 1):
    temp = [0] * 10
    num_str = str(i)

    for digit in num_str:
        temp[int(digit)] += 1

    cnt1 = 0
    cnt2 = 0
    for count in temp:
        if count == 1:
            cnt1 += 1

        if count > 0 :
            cnt2 += 1

    if cnt1 == 1 and cnt2 == 2:
        ans += 1

print(ans)