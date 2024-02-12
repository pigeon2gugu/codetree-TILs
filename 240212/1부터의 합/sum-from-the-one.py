n = int(input())

sumVal = 0

for i in range(1, 100+1) :
    sumVal += i
    if sumVal >= n :
        break

print(i)