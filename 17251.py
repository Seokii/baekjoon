n = int(input())
arr = list(map(int, input().split()))

max_value = max(arr)
search = []
cnt = 0

for i in arr:
    if i == max_value:
        search.append(cnt)
    cnt += 1

if len(search) > 1:
    start = search[0]
    end = search[-1]
    B = start
    X = end - start
    R = n - 1 - B - X
else:
    B = search[0]
    R = n-1-B

if B > R: print('B')
elif R > B: print('R')
else: print('X')