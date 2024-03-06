arr = []

while True :
    age = int(input())

    if age // 10 != 2 :
        break

    arr.append(age)

print(f"{sum(arr)/len(arr):.2f}")