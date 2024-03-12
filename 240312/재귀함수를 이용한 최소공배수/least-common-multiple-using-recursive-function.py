n = int(input())
arr = list(map(int, input().split()))

def getDiv(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def getMulti(a, b):
    return a * b // getDiv(a, b)


def getNumber(n):
    if n == 0:
        return arr[0]
    
    return getMulti(arr[n], getNumber(n-1))

print(getNumber(n-1))