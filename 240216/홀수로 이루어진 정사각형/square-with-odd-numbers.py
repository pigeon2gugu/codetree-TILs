n = int(input())

num = 11
for i in range(n) :
    for j in range(n) :
        print(num + 2*j, end = " ")
    num += 2
    print()