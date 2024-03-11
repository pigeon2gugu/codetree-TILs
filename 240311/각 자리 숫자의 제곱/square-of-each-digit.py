n = int(input())

def getDigit(n) :
    if n < 10 :
        return n**2

    return getDigit(n // 10) + (n % 10)**2


print(getDigit(n))