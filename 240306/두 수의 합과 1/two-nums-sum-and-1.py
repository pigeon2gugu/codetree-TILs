a, b = tuple(map(int, input().split()))

sumVal = str(a + b)

cnt = 0
for elem in sumVal :
    if elem == "1" :
        cnt += 1

print(cnt)