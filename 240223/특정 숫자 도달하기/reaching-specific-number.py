arr = list(map(int, input().split()))

sumVal = 0
length = 0
for elem in arr :
    if elem >= 250 :
        break

    sumVal += elem
    length += 1

print(f"{sumVal} {sumVal/length:.1f}")