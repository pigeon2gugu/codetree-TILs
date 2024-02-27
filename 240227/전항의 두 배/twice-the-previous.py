arr = list(map(int, input().split()))
answer = [arr[0], arr[1]]

for i in range(2, 10) :
    answer.append(answer[i-1] + 2 * answer[i-2])

for elem in answer :
    print(elem, end = " ")