arr = list(map(int, input().split()))

answer = [0 for i in range(10)]
answer[0], answer[1] = arr[0], arr[1]

for i in range(2, 10) :
    answer[i] = (answer[i-1] + answer[i-2]) % 10

for elem in answer :
    print(elem, end = " ")