import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

# 시작 지점 찾기
for i in range(N):
    for j in range(M):
        if data[i][j] == 2:
            visited[i][j] = True
            data[i][j] = 0
            start = (i, j)

def BFS(start, data, visited):
    queue = deque()
    queue.append(start)

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy

            if (0 <= nx < N) and (0 <= ny < M) and (not visited[nx][ny]) and data[nx][ny] != 0:
                visited[nx][ny] = True
                data[nx][ny] = data[x][y] + 1
                queue.append((nx, ny))

    for i in range(N):
        for j in range(M):
            if (visited[i][j] == False) and (data[i][j] != 0):
                data[i][j] = -1
    
    for d in data:
        print(" ".join(map(str, d)))

BFS(start, data, visited)