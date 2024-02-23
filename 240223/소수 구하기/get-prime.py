n = int(input())

for i in range(1, n+1) :

    if i == 1 :
        continue

    isTrue = True
    for j in range(2, i) :
        if i % j == 0 :
            isTrue = False
            break

    if isTrue :
        print(i, end = " ")