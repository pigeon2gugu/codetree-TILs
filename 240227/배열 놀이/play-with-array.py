n, q = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

for _ in range(q) :
    questions = list(map(int, input().split()))
    question = questions[0]
    if question == 1 :
        print(arr[questions[1] - 1])
    elif question == 2 :
        if questions[1] in arr :
            print(arr.index(questions[1]) + 1)
        else :
            print(0)
    elif question == 3:
        for j in range(questions[1], questions[2] + 1) :
            print(arr[j - 1], end = " ")
        print()