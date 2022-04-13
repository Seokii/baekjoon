t = int(input())

for _ in range(t):
    b,d = input().split()
    b = int(b)
    tmp = 0
    # print(int(d, b) % (b - 1))

    """
    for i in range(len(d)):
        tmp += int(d[i])
    """

    tmp = sum(map(int, list(d)))
    print(tmp % (b-1))