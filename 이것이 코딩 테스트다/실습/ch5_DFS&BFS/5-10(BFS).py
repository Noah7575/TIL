from collections import deque

# BFS로 풀기
n, m = map(int, input().split())
# 맵 입력 - 리스트 컴프리헨션
graph = [list(map(int, input().split())) for _ in range(n)]

# 이동 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS
def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 1 # 방문 처리

    while queue:
        x, y = queue.popleft()

        for i in range(4): # 네 방향 이동 체크
            nx, ny = x + dx[i], y + dy[i]

            # 맵 범위를 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 음료수 채우기
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny))

# 덩어리 개수 세기
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            bfs(i, j)
            result += 1

print(result)    
        
