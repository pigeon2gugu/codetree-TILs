arr = list(map(int, input().split()))
n, m = arr[0], arr[1]

for _ in range(n) :
    for _ in range(m) :
        print("*", end = " ")
    print()