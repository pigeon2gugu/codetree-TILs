n = int(input())

isTrue = True

for i in range(2, n) :
    if n % i == 0 :
        isTrue = False
        break

if isTrue :
    print("N")
else :
    print("C")