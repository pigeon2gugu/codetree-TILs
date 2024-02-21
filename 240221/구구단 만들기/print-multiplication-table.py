arr = list(map(int, input().split()))
a, b = arr[0], arr[1]

for i in range(1, 10) :
    for j in range(b, a-2, -2) :
        print(f"{j} * {i} = {i*j}", end = " ")
        if j > a :
            print("/ ", end = "")
    print()