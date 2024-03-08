s = input()

def hasDuplicateAlpha(string) :

    if len(string) <= 1 :
        return False

    temp = string[0]
    cnt = 1
    for i in range(1, len(string)-1) :
        if temp not in string[i:-1] :
            cnt += 1

        if cnt == 2 :
            return True

        temp = string[i]
    
    return False


if hasDuplicateAlpha(s) :
    print("Yes")
else :
    print("No")