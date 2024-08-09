x, y = tuple(map(int, input().split()))
ans = 0

for i in range(x, y + 1) :
    cnt = 0
    temp = [0] * 10

    for j in range(len(str(i))) :
        temp[int(str(i)[j])] += 1

    for j in range(len(temp)) :
        if (temp[j]) == 1 :
            cnt += 1

    if cnt == 1 :
        ans += 1
        


print(ans)