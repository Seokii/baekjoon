import sys
sys.setrecursionlimit(10 ** 6) # 재귀 런타임 에러 해결 코드(허용 깊이를 늘려줌)

def dfs(x,y):
    if x <= -1 or x >= h or y <= -1 or y >= w:
        return False
    if graph[x][y] == "#":
        graph[x][y] = "."
        cnt.append(1)

        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)

        return True
    return False

t = int(input())
res = []
temp = []

for _ in range(t):
    cnt = []
    h,w = map(int, input().split())
    graph = [list(map(str, input().strip())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j] == "#":
                dfs(i,j)
                temp.append(len(cnt))
                cnt = []

    print(len(temp))
    temp = []