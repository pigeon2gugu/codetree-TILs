n = int(input())

def getNumber(n) :
    if n == 1 :
        return 2
    
    if n == 2 :
        return 4

    return getNumber(n-2) * getNumber(n-1) % 100


print(getNumber(n))