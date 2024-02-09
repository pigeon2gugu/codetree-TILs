n = int(input())

sumVal = 0
for i in range(n) :
    temp = int(input())
    if temp % 2 == 1 and temp % 3 == 0 :
        sumVal += temp

print(sumVal)