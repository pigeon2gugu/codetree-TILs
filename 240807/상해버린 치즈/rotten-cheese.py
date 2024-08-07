n, m, d, s = tuple(map(int, input().split()))

arr1 = [
    tuple(map(int, input().split()))
    for _ in range(d)
]

arr2 = [
    tuple(map(int, input().split()))
    for _ in range(s)
]
ans = 0

for i in range(m) :
    cnt = 0

    for j in range(s) :
        for k in range(d) :
            if arr1[k][1] == i and arr1[k][0] == arr2[j][0] and arr1[k][2] < arr2[j][1] :
                cnt += 1

    if cnt == s :
        patientCnt = [0] * (n + 1)
        for k in range(d) :
            if arr1[k][1] == i :
                patientCnt[arr1[k][0]] = 1

        ans = max(ans, sum(patientCnt))

print(ans)