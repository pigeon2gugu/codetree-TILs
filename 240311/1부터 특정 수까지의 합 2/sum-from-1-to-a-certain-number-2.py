n = int(input())

def sumNumber(n) :
    if n == 1:
        return 1

    return sumNumber(n-1) + n


print(sumNumber(n))