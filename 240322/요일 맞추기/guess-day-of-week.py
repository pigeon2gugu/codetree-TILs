m1, d1, m2, d2 = tuple(map(int, input().split()))

def getDate(m, d) :
    dayOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return sum(dayOfMonth[:m-1]) + d


m1Date = getDate(m1, d1)

def getDay(m, d) :
    dif = (getDate(m, d) - m1Date) % 7
    day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    return day[dif]


print(getDay(m2, d2))