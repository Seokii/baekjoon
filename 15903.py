n,m = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(m):
    arr.sort()
    tmp = arr[0] + arr[1]
    arr[0] = tmp
    arr[1] = tmp

print(sum(arr))