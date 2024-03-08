n, m = tuple(map(int, input().split()))
arrA = list(map(int, input().split()))

def getSumArrA() :

    for _ in range(m) :
        sumVal = 0
        a, b = tuple(map(int, input().split()))
        sumVal += sum(arrA[a-1:b])
        print(sumVal)


getSumArrA()