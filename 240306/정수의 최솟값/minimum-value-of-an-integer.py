a, b, c = tuple(map(int, input().split()))

def getMin(*args) :
    return min(args)


print(getMin(a, b, c))