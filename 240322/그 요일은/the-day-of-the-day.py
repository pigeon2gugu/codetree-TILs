m1, d1, m2, d2 = tuple(map(int, input().split()))
day = input()

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def getDate(m, d) :
    dayOfMonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return sum(dayOfMonth[:m-1]) + d

cnt = (getDate(m2, d2) - getDate(m1, d1)) // 7

if (getDate(m2, d2) - getDate(m1, d1)) % 7 >= days.index(day) :
    cnt += 1


print(cnt)