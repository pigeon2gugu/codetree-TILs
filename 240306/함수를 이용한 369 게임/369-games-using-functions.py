a, b = tuple(map(int, input().split()))

def isMultipleOf3(num) :
    return num % 3 == 0

def isYourNumber(num) :
    isTrue = False
    for elem in str(num) :
        if elem == "3" or elem == "6" or elem == "9" :
            isTrue = True
            break

    if isMultipleOf3(num) :
        isTrue = True

    return isTrue


cnt = 0
for i in range(a, b+1) :
    if isYourNumber(i) :
        cnt += 1

print(cnt)