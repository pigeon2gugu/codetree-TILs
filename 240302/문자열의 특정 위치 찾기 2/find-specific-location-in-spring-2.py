arr = ["apple", "banana", "grape", "blueberry", "orange"]
s = input()
answer = []

for elem in arr :
    if elem[2] == s or elem[3] == s :
        answer.append(elem)

for elem in answer :
    print(elem)

print(len(answer))