arr = list(map(int, input().split()))
answer = [0 for _ in range(10)]

for elem in arr :
    if elem == 0 :
        break
    
    if elem < 10 :
        continue

    answer[elem//10 - 1] += 1

for i in range(len(answer)-1, -1, -1) :
    print(f"{(i+1) * 10} - {answer[i]}")