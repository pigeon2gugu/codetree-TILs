n, m = tuple(map(int, input().split()))

def printNum(n, m) :
    
    if n > m :
        num = m
    else :
        num = n

    for i in range(n, 0, -1) :
        if n % i == 0 and m % i == 0 :
            print(i)
            break


printNum(n, m)