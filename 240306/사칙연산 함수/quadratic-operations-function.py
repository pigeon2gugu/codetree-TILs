a, o, c = tuple(input().split())
a = int(a)
c = int(c)

def addCalculator(a, b) :
    return a + b

def diffCalculator(a, b) :
    return a - b

def multipleCaculator(a, b) :
    return a * b

def divCalculator(a, b) :
    return a // b


def calculator(a, o, c) :

    expression = f"{a} {o} {c} = "
    if o == "+" :
        return expression + str(addCalculator(a, c))
    elif o == "-" :
        return expression + str(diffCalculator(a, c))
    elif o == "*" :
        return expression + str(multipleCaculator(a, c))
    elif o == "/" :
        return expression + str(divCalculator(a, c))
    else :
        return "False"


print(calculator(a, o, c))