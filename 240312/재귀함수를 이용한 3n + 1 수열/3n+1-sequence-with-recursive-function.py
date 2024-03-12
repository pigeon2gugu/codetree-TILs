n = int(input())

def getNumber(n) :
    if n <= 1 :
        return 0

    if n % 2 == 0 :
        return getNumber(n//2) + 1
    else :
        return getNumber(n*3 + 1) + 1


print(getNumber(n))