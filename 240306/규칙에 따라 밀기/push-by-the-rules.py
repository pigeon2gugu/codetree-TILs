s = input()
q = input()

for quest in q :
    if quest == "R" :
        s = s[-1] + s[:-1]
    elif quest == "L" :
        s = s[1:] + s[0]

print(s)