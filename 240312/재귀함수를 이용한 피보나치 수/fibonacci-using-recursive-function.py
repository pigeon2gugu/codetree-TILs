n = int(input())

def getPibo(n) :
    if n == 1 :
        return 1
    
    if n == 2 :
        return 1

    return getPibo(n-2) + getPibo(n-1)


print(getPibo(n))