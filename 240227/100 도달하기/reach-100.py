n = int(input())
answer = [0, 0]
answer[0] = 1
answer[1] = n

cnt = 2
while True :
    answer.append(answer[cnt - 1] + answer[cnt - 2])
    cnt += 1

    if answer[-1] > 100 :
        break

for elem in answer :
    print(elem, end = " ")