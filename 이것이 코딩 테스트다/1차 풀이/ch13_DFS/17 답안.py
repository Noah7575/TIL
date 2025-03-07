from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보
data = [] # 바이러스 정보

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            # 바이러스 종류, 시간, 위치 X, 위치 Y 삽입
            data.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
queue = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 바이러스 진행방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS
while queue:
    virus, s, x, y = queue.popleft()
    # 정확히 s초가 지났거나, 큐가 빌 때까지 반복
    if s == target_s:
        break
    # 현재 노드에서 주변 4가지 위치 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동 가능한 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 아직 방문하지 않은 위치라면 바이러스 넣기(시간 + 1)
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                queue.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])
