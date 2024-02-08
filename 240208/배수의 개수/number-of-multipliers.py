cnt3 = 0
cnt5 = 0
for _ in range(10) :
    temp = int(input())
    if temp % 3 == 0 :
        cnt3 += 1
    if temp % 5 == 0 :
        cnt5 += 1

print(cnt3, cnt5, end = " ")