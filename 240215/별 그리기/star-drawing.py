n = int(input())

for i in range(n-1) :
    for _ in range(n-1-i) :
        print(" ", end = "")
    for _ in range(2*i + 1) :
        print("*", end ="")
    print()

for i in range(n, 0, -1) :
    for _ in range(n-i) :
        print(" ", end = "")
    for _ in range(i*2 -1) :
        print("*", end = "")
    print()