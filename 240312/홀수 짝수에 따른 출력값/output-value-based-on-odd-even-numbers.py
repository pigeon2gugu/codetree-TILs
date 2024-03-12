n = int(input())

def getNumber(n) :
    if n == 1 :
        return 1
    
    if n == 2 :
        return 2

    if n % 2 == 0 :
        return getNumber(n-2) + n
    else :
        return getNumber(n-2) + n


print(getNumber(n))