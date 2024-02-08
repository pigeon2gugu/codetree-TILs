n = int(input())

for _ in range(n) :
    temp = int(input())
    if temp % 2 == 1 and temp % 3 == 0 :
        print(temp)