n = int(input())

for i in range(1, n+1) :
    for j in range(1, n+1) :
        if j % 2 == 0 :
            print(n+1-i, end = "")
        else :
            print(i, end = "")
    print()