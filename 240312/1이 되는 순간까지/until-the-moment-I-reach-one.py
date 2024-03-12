n = int(input())
cnt = 0

def calculate(n) :
    global cnt
    if n == 1 :
        return cnt

    if n % 2 == 0:
        cnt += 1
        return calculate(n // 2)
    else :
        cnt += 1
        return calculate(n // 3)


print(calculate(n))