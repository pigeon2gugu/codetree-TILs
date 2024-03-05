a = input()
b = input()

while True :
    idx = a.find(b)

    if idx == -1 :
        break

    a = a[:idx] + a[idx+len(b):]
    

print(a)