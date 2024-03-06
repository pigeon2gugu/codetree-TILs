n = input()

def isYourNumber(strNum) :

    isTrue = True
    if int(strNum) % 2 != 0 :
        isTrue = False

    sumVal = 0
    for elem in strNum :
        sumVal += int(elem)

    if sumVal % 5 != 0 :
        isTrue = False

    if isTrue :
        return "Yes"
    else :
        return "No"


print(isYourNumber(n))