s = input()
n = int(input())

for elem in s[-1:len(s)-n-1:-1] :
    print(elem, end = "")