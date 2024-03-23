n = input()
num = 0
digits = []

for nn in n :
    num = num * 2 + int(nn)

num *= 17

while True :
    if num < 2 :
        digits.append(num)
        break

    digits.append(num%2)
    num //= 2

for digit in digits[::-1] :
    print(digit, end = "")