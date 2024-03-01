s1, s2 = tuple(input().split())

if len(s1) > len(s2) :
    print(s1, len(s1), end = " ")
elif len(s2) > len(s1) :
    print(s2, len(s2), end = " ")
else :
    print("same", len(s1))