a, b = tuple(map(int, input().split()))

def isPrime(num) :
    for i in range(2, num)  :
        if num % i == 0 :
            return False

    return True

def sumOfPrime(a, b) :
    sumVal = 0
    for i in range(a, b+1) :
        if isPrime(i) :
            sumVal += i

    return sumVal


print(sumOfPrime(a,b))