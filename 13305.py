n = int(input())
distance = list(map(int, input().split()))
oil_price = list(map(int, input().split()))
del oil_price[-1]

tmp_price = oil_price[0]
cost = 0

for i in range(len(distance)):
    if tmp_price > oil_price[i]:
        tmp_price = oil_price[i]
    cost += tmp_price * distance[i]

print(cost)