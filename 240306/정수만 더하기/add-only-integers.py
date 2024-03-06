s = input()

answer = 0

for elem in s :
    if elem.isdigit() :
        answer += int(elem)

print(answer)