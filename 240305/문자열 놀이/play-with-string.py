s, q = tuple(input().split())
q = int(q)

arr = list(s)

for i in range(q) :
    quest = input().split()

    if quest[0] == "1" :
        temp = arr[int(quest[1])-1]
        arr[int(quest[1])-1] = arr[int(quest[2])-1]
        arr[int(quest[2])-1] = temp

    elif quest[0] == "2" :
        for j in range(len(arr)) :
            if arr[j] == quest[1] :
                arr[j] = quest[2]

    answer = ''.join(arr)
    print(answer)