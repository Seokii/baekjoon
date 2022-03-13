from collections import deque

n,m = map(int, input().split())
hx,hy = map(int, input().split())
ex,ey = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[[-1, -1] for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((hx-1, hy-1, 0))
    visited[hx-1][hy-1][0] = 0
    while queue:
        x,y,z = queue.popleft()
        if x == ex-1 and y == ey-1:
            return visited[x][y][z]
        for i in range(4):
            nx, ny, nz = x+dx[i], y+dy[i], z
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny]:
                if nz:
                    continue
                else:
                    nz = 1
            if visited[nx][ny][nz] == -1:
                visited[nx][ny][nz] = visited[x][y][z]+1
                queue.append((nx, ny, nz))
    return -1

print(bfs())