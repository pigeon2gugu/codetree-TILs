arr = [list(map(int, input().split())) for _ in range(2)]

print(f"{(sum(arr[0])/4):.1f} {(sum(arr[1])/4):.1f}")

totalSum = 0
for i in range(4) :
    tempSum = 0
    for j in range(2) :
        tempSum += arr[j][i]
        totalSum += arr[j][i]
    print(f"{tempSum/2:.1f}", end = " ")

print()

print(f"{(totalSum/8):.1f}")