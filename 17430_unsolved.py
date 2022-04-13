import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    arr1 = []
    arr2 = []
    tmp1_set = []
    tmp2_set = []
    n = int(input())
    answer = ""
    for _ in range(n):
        tmp1, tmp2 = (map(int, input().split()))
        arr1.append(tmp1)
        arr2.append(tmp2)
    if n % 2 != 0:
        answer = "NOT BALANCED"
        break

    tmp1_set = set(arr1)
    tmp1_set = list(tmp1_set)
    tmp2_set = set(arr2)
    tmp2_set = list(tmtsp2_set)
    for i in tmp1_set:
        pos = arr1.count(i)
        neg = arr1.count(i * -1)
        if pos != neg:
            answer = "NOT BALANCED"
            break

    for i in tmp2_set:
        if arr2.count(i) % 2 != 0:
            answer = "NOT BALANCED"
            break

    if len(answer) == 0:
        answer = "BALANCED"

    print(answer)