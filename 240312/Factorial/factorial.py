n = int(input())

def getFactorial(n) :
    if n == 0 :
        return 1

    return getFactorial(n-1) * n


print(getFactorial(n))