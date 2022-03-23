t = int(input())

for _ in range(t):
    n = int(input())
    credit = 0.0
    total = 0.0
    for _ in range(n):
        c,g = map(float, input().split())
        credit += c
        total += round(g*c, 1)
    gpa = round(total / credit, 1)
    credit = int(credit)
    print(f'{credit} {gpa}')