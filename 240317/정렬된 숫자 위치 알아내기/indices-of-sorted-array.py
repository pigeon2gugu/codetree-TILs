n = int(input())
arr = list(map(int, input().split()))

class Number:
    def __init__(self, value, index):
        self.value = value
        self.index = index

numbers = [Number(v, idx) for idx, v in enumerate(arr, start=1)]
sortedNumbers = sorted(numbers, key=lambda x: x.value)

answer = []

for n in numbers:
    for idx, num in enumerate(sortedNumbers, start = 1):
        if num.index == n.index:
            answer.append(idx)
            break

for elem in answer:
    print(elem, end=" ")