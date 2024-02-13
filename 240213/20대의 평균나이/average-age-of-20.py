sumVal = 0
cnt = 0

while True :
    n = int(input())

    if n // 10 != 2 :
        break
    
    sumVal += n
    cnt += 1

print(f"{sumVal/cnt:.2f}")