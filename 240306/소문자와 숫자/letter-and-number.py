s = input()

answer = ""
for elem in s :
    if elem.isdigit() :
        answer += elem
    elif elem.isalpha() :
        answer += elem.lower()

print(answer)