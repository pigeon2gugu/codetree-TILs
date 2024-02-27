arr = list(map(int, input().split()))
answer = []

for elem in arr :
    if elem == 0 :
        break
    
    if elem % 2 == 0 :
        answer.append(elem//2)
    else :
        answer.append(elem + 3)

for elem in answer :
    print(elem, end = " ")