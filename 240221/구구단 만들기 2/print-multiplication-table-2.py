arr = list(map(int, input().split()))
a, b = arr[0], arr[1]

for i in range(2, 10, 2) :
    for j in range(b, a-1, -1) :
        print(f"{j} * {i} = {i*j}", end = " ")
        if j > a :
            print("/", end = " ")
    print()