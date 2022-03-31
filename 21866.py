arr = list(map(int, input().split()))
hacker = 0
no_coffee = 0

if arr[0] > 100 or arr[1] > 100 or arr[2] > 200 or \
    arr[3] > 200 or arr[4] > 300 or arr[5] > 300 or \
    arr[6] > 400 or arr[7] > 400 or arr[8] > 500:
    hacker += 1
elif sum(arr) < 100:
    no_coffee += 1

if hacker == 1: print("hacker")
elif no_coffee == 1: print("none")
else: print("draw")