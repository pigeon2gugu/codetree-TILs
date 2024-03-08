a, b = tuple(map(int, input().split()))

def doCalculate(a, b) :
    if a < b :
        a = a + 10
        b = b * 2
    else :
        a = a * 2
        b = b + 10

    return a, b


a, b = doCalculate(a, b)
print(a, b)