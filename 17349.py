import sys
input = sys.stdin.readline

answer = []
not_answer = []
predict = []
for i in range(9):
    predict.append(list(map(int, input().split())))

for i in range(9):
    first_base = []
    not_first_base = []
    if predict[i][0] == 1:
        predict[i][0] = 0
    else: predict[i][0] = 1

    for j in range(9):
        if predict[j][0] == 1:
            first_base.append(predict[j][1])
        else:
            not_first_base.append(predict[j][1])

    tmp = set(first_base)
    first_base = list(tmp)
    tmp = set(not_first_base)
    not_first_base = list(tmp)

    for k in first_base:
        if len(first_base) == 1 and k in first_base and k not in not_first_base:
            answer.append(k)
        else:
            not_answer.append(k)

    if len(first_base) == 0:
        for l in range(1, 10):
            if l not in not_first_base:
                answer.append(l)

    if predict[i][0] == 0:
        predict[i][0] = 1
    else: predict[i][0] = 0


tmp = set(answer)
answer = list(tmp)
tmp = set(not_answer)
not_answer = list(tmp)

if len(answer) == 1:
    print(answer[0])
elif len(not_answer) == 9:
    print(-1)
elif len(answer) == 0:
    tmp = []
    for i in range(1, 10):
        if i not in not_answer:
            tmp.append(i)
    if len(tmp) == 1:
        print(tmp[0])
    else:
        print(-1)
else:
    print(-1)