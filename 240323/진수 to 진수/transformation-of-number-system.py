a, b = tuple(map(int, input().split()))
n = input()
digits = []

num = 0
for nn in n :
    num = num * a + int(nn)

while True :
    if num < b :
        digits.append(num)
        break

    digits.append(num%b)
    num //= b

for digit in digits[::-1] :
    print(digit, end = "")