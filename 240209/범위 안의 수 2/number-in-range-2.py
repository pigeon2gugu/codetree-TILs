sumVal = 0
cnt = 0

for _ in range(10) :
    num = int(input())
    if num >= 0 and num <= 200 :
        sumVal += num
        cnt += 1

print(f"{sumVal} {sumVal/cnt:.1f}")