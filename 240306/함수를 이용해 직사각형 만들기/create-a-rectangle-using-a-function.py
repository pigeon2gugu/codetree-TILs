n, m = tuple(map(int, input().split()))

def printSquare(n1, n2) :
    for _ in range(n1) :
        print("1" * n2)


printSquare(n, m)