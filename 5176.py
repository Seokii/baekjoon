k = int(input())
for _ in range(k):
    p,m = map(int, input().split())

    seats = []
    for i in range(1,m+1): seats.append(i)

    participant = []
    for _ in range(p): participant.append(int(input()))
    participant_set = set(participant)
    participant = list(participant_set)

    tmp = 0
    answer = 0
    for i in participant:
        if i in seats:
            tmp += 1
    answer = p-tmp
    print(answer)
    tmp=0
    answer=0