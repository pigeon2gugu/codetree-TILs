n = int(input())

cnt = 1
for i in range(n) :
    for j in range(cnt) :
        print("*", end="")
    print()
    cnt += 2