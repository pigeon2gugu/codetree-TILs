n = int(input())

sumVal = 0

for i in range(1, n) :
    if n % i == 0 :
        sumVal += i

if sumVal == n :
    print("P")
else :
    print("N")