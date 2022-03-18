import sys, itertools
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
accumulate = list(itertools.accumulate(arr))
m = int(input())
for _ in range(m):
    start,end = map(int, input().split())
    # print(sum(arr[start-1:end])) 시간초과 발생
    if start == 1:
        print(accumulate[end-1])
    else:
        print(accumulate[end-1]-accumulate[start-2])