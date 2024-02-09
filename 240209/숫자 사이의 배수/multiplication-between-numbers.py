arr = list(map(int, input().split()))
a, b = arr[0], arr[1]

sumVal = 0
cnt = 0
for i in range(a, b+1) :
    if i % 5 == 0 or i % 7 == 0 :
        sumVal += i
        cnt += 1


print(f"{sumVal} {sumVal/cnt:.1f}")