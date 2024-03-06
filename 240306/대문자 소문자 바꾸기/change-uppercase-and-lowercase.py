s = input()


for elem in s :
    if "A" <= elem and elem <= "Z" :
        print(elem.lower(), end = "")
    else :
        print(elem.upper(), end = "")