n = int(input())
arr = []

for _ in range(n) :
    arr.append(int(input()))

sumVal = 0
for elem in arr :
    sumVal += elem

sumVal = str(sumVal)

print(sumVal[1:] + sumVal[0])