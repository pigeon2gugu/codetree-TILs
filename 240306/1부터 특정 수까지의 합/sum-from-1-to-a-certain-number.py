n = int(input())

def calculate(num) :
    sumVal = 0
    for i in range(1, num+1) :
        sumVal += i
    
    return sumVal//10


print(calculate(n))