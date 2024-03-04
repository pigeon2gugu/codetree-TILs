arr = [input() for _ in range(10)]
s = input()

answer = []

for elem in arr :
    if elem[-1] == s :
        answer.append(elem)

if len(answer) == 0 :
    print("None")
else :
    for elem in answer :
        print(elem)