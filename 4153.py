import math

while True:
    arr = list(map(int, input().split()))
    if sum(arr) == 0:
        break
    arr.sort(reverse=True)
    if math.pow(arr[0],2) == math.pow(arr[1],2) + math.pow(arr[2],2):
        print("right")
    else:
        print("wrong")