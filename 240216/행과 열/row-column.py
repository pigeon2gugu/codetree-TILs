arr = list(map(int, input().split()))
a, b = arr[0], arr[1]

for i in range(1, a+1) :
    for j in range(1, b+1) :
        print(i*j, end = " ")
    print()