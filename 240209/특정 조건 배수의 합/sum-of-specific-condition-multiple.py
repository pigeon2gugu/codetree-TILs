arr = list(map(int, input().split()))
a, b = arr[0], arr[1]

sumVal = 0

if b >= a :
    for i in range(a, b+1) :
        if i % 5 == 0 :
            sumVal += i
else :
    for i in range(b, a+1) :
        if i % 5 == 0 :
            sumVal += i

print(sumVal)