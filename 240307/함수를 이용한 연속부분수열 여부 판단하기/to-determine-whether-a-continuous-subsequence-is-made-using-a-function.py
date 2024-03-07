n1, n2 = tuple(map(int, input().split()))
arrA = list(input().split())
arrB = list(input().split())

def isBInA(a, b) :
    strA = ''.join(a)
    strB = ''.join(b)

    if strB in strA :
        return True

    return False


if isBInA(arrA, arrB) :
    print("Yes")
else :
    print("No")