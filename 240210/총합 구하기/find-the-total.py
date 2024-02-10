arr = list(map(int, input().split()))

a, b = arr[0], arr[1]

sumVal = 0
for i in range(a, b+1) :
    if i % 6 == 0 and i % 8 != 0 :
        sumVal += i

print(sumVal)