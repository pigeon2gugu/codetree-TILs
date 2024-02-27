arr = list(map(int, input().split()))
a, b = arr[0], arr[1]

answer = [0 for _ in range(b)]

while a > 1 :
    answer[a%b] += 1
    a = a//b

sumVal = 0
for i in range(len(answer)) :
    sumVal += answer[i] ** 2

print(sumVal)