arr = input().split()

w = int(arr[0])
h = int(arr[1])

w += 8
h *= 3

print(w, h, w*h, sep = "\n")