n = int(input())
arr = list(map(int, input().split()))

class Number :
    def __init__(self, value, index) :
        self.value = value
        self.index = index

numbers = [Number(value, idx) for idx, value in enumerate(arr, start = 1)]

numbers.sort(key = lambda x : x.value)

answer = [0 for _ in range(n)]

for idx, n in enumerate(numbers, start = 1) :
    answer[n.index - 1] = idx

for a in answer :
    print(a, end = " ")