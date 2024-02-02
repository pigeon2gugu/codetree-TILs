arr = list(map(int, input().split()))

h = arr[0]
w = arr[1]

bmi = int(w // (h * 0.01)**2)

print(bmi)
if bmi >= 25 :
    print("Obesity")