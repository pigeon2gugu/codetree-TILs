arr = [input() for _ in range(10)]
s = input()


for elem in arr :
    if elem[-1] == s :
        print(elem)