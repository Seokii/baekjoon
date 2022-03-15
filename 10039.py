score = []
for _ in range(5):
    tmp = int(input())
    if tmp < 40: tmp = 40
    score.append(tmp)

print(sum(score)//len(score))