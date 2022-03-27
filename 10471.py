w,p = map(int, input().split())
l = list(map(int, input().split()))

answer = []
answer.append(w)

for i in range(len(l)):
    answer.append(l[i])
    answer.append(w-l[i])
    for j in range(i):
        answer.append(l[i]-l[j])

answer = set(answer)
answer = list(answer)
answer.sort()

for i in range(len(answer)):
    print(answer[i], end=' ')