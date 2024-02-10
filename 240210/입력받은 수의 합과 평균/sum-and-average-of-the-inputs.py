n = int(input())

sumVal = 0
cnt = 0

for _ in range(n) :
    num = int(input())
    sumVal += num
    cnt += 1

print(f"{sumVal} {sumVal/cnt:.1f}")