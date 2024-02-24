arr = list(map(int, input().split()))

sumVal2 = 0
sumVal3 = 0
cnt3 = 0

for i in range(len(arr)) :
    if (i+1) % 2 == 0 :
        sumVal2 += arr[i]
    if (i+1) % 3 == 0 :
        sumVal3 += arr[i]
        cnt3 +=1

print(f"{sumVal2} {sumVal3/cnt3:.1f}")