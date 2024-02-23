arr = list(map(int, input().split()))

sumVal = 0
cnt = 0

for elem in arr :
    if elem == 0 :
        break
    
    elif elem % 2 == 0 :
        sumVal += elem
        cnt += 1

print(f"{cnt} {sumVal}")