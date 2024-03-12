n = int(input())

def getNumber(n) :
    if n == 1 :
        return 1
    
    if n == 2 :
        return 2

    return getNumber(n//3) + getNumber(n-1)


print(getNumber(n))