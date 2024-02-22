n = int(input())

cnt = ord("A")

for i in range(n) :
    for j in range(i) :
        print(" ", end = " ")
    for j in range(n-i) :
        print(chr(cnt), end = " ")
        if chr(cnt) == "Z" :
            cnt = ord("A")
        else :
            cnt += 1
    print()