n = int(input())

cnt = 2

for _ in range(n) :
    for _ in range(n) :
        if cnt > 8 :
            cnt = 2
        print(cnt, end = " ")
        cnt += 2
    print()