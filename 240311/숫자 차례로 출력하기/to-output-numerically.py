n = int(input())

def print1toN(n) :
    if n == 0 :
        return

    print1toN(n-1)
    print(n, end = " ")


def printNto1(n) :
    if n == 0 :
        return

    print(n, end = " ")
    printNto1(n-1)


print1toN(n)
print()
printNto1(n)