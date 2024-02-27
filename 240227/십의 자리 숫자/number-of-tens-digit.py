arr = list(map(int, input().split()))
answer = [0 for _ in range(9)]

for elem in arr :

    if elem == 0 :
        break

    if elem < 10 :
        continue

    answer[elem//10 - 1] += 1

for i in range(len(answer)) :
    print(f"{i+1} - {answer[i]}")