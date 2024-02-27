symptom = []
temp = []

for _ in range(3) :
    arr = list(input().split())
    symptom.append(arr[0])
    temp.append(int(arr[1]))

cnt = [0] * 4

for i in range(3) :
    if symptom[i] == "Y" and temp[i] >= 37 :
        cnt[0] += 1
    elif symptom[i] == "N" and temp[i] >= 37 :
        cnt[1] += 1
    elif symptom[i] == "Y" and temp[i] < 37 :
        cnt[2] += 1
    else :
        cnt[3] += 1

for elem in cnt :
    print(elem, end = " ")

if cnt[0] >= 2 :
    print("E")