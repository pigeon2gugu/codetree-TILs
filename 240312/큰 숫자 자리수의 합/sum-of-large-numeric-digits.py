a, b, c = tuple(list(map(int, input().split())))

n = a * b * c

def getNumber(n) :

    if n < 10 :
        return n

    return getNumber(n // 10) + (n % 10)


print(getNumber(n))