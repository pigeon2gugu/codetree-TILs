n = int(input())

def printNumber(n) :
    if n == 0 :
        return

    print(n, end = " ")
    printNumber(n-1)
    print(n, end = " ")


printNumber(n)