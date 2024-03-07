y, m, d = tuple(map(int, input().split()))

def getSeason(month) :

    if month >= 3 and month <= 5 :
        return "Spring"
    elif month >= 6 and month <= 8 :
        return "Summer"
    elif month >= 9 and month <= 11 :
        return "Fall"
    else :
        return "Winter"


def isLeapYear(year) :
    if year % 4 != 0 :
        return False

    if year % 4 == 0 and year % 100 == 0 and year % 400 != 0 :
        return False

    return True


def isValidate(year, month, day) :
    day31Month = [1, 3, 5, 7, 8, 10, 12]

    if month == 2 :
        if isLeapYear(year) and day <= 29 :
            return True
        else :
            return False
    
    if month in day31Month :
        if day <= 31 :
            return True
        else :
            return False

    else :
        if day < 30 :
            return True
        else :
            return False


if isValidate(y, m ,d) :
    print(getSeason(m))
else :
    print(-1)