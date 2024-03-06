s, q = tuple(input().split())
q = int(q)

for _ in range(q) :
    quest = int(input())

    if quest == 1 :
        s = s[1:] + s[0]
    elif quest == 2 :
        s = s[-1] + s[:-1]
    elif quest == 3 :
        s = s[-1::-1]

    print(s)