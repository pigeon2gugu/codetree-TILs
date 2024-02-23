n = int(input())

for _ in range(n) :
    arr = list(map(int, input().split()))
    a, b = arr[0], arr[1]

    sumVal = 0
    for i in range(a, b+1) :
        if i % 2 == 0 :
            sumVal += i
    print(sumVal)