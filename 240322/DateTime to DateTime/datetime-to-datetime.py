d, h, m = tuple(map(int, input().split()))

def getMin(d, h, m) :
    dayToMin = (d-1) * 60 * 24
    hourToMin = (h) * 60

    return dayToMin + hourToMin + m

diffMin = getMin(d, h, m) - getMin(11, 11, 11)

if diffMin < 0 :
    print(-1)
else :
    print(diffMin)