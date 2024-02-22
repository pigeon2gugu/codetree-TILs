n = int(input())

cnt = ord("A")

for i in range(1, n+1) :
    for j in range(i) :
        print(chr(cnt), end = "")
        if chr(cnt) == "Z" :
            cnt = ord("A")
        else :
            cnt += 1
    print()