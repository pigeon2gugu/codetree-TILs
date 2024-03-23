n, d = tuple(map(int, input().split()))
digits = []

while True :
    if n < d :
        digits.append(n)
        break

    digits.append(n%d)
    n //= d


for digit in digits[::-1] :
    print(digit, end = "")