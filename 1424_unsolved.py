n = int(input())
l = int(input())
c = int(input())

total = n * l
"""
answer = 1
songs_in_cd = 0
tmp = 0
while True:
    tmp += (l+1)
    n -= 1
    songs_in_cd += 1
    if tmp > c:
        if (songs_in_cd-1) % 13 == 0:
            n += 1
        tmp = 0
        songs_in_cd = 0
        n += 1
        answer += 1
    if n == 0 and songs_in_cd % 13 == 0:
        answer += 1
    if n == 0 : break

print(answer)
"""