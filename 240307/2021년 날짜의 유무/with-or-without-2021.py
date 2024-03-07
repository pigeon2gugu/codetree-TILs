m, d = tuple(map(int, input().split()))

def hasDateInMonth(m, d) :

    day31Month = [1, 3, 5, 7, 8, 10, 12]
    if m > 12 or d > 31 :
        return False

    if m == 2 and d <= 28:
        return True

    if m in day31Month :
        if d <= 31 :
            return True
        else :
            return False

    else :
        if d <= 30 :
            return True
        else :
            return False


if hasDateInMonth(m, d) :
    print("Yes")
else :
    print("No")