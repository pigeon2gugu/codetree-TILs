n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

def changeArr() :
    global m

    sumVal = 0

    while m >= 1 :

        sumVal += arr[m-1]

        if m % 2 != 0 :
            m -= 1
        else :
            m //= 2

        
    return sumVal


print(changeArr())