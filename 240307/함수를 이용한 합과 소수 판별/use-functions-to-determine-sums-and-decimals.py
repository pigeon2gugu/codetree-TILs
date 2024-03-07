a, b = tuple(map(int, input().split()))

def isPrime(n) :
    if n <= 1 :
        return False

    for i in range(2, n) :
        if n % i == 0 :
            return False

    return True


def isEvenForAllNumber(n) :

    num = 0
    while n > 0 :
        num += n%10
        n //= 10

    if num % 2 == 0 :
        return True
    
    return False
    

def getCount(a, b) :
    
    cnt = 0
    for i in range(a, b+1) :
        if isPrime(i) and isEvenForAllNumber(i) :
            cnt += 1

    return cnt


print(getCount(a, b))