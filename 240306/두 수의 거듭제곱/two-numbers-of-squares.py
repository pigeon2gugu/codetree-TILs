a, b = tuple(map(int, input().split()))

def printNum(a, b) :

    num = 1
    for _ in range(b) :
        num *= a

    print(num)



printNum(a, b)