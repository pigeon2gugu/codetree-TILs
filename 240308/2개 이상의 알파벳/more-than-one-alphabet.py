s = input()

def hasDuplicateAlpha(string) :

    if len(string) <= 1 :
        return False

    firstAlpha = string[0]
    if firstAlpha in string[1:] :
        return False
    
    return True


if hasDuplicateAlpha(s) :
    print("Yes")
else :
    print("No")