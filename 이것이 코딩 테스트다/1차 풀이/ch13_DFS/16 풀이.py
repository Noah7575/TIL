from itertools import combinations
from collections import deque
import copy
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

data = []

# 맵 입력받기
for i in range(N):
    temp = list(map(int, input().split()))
    data.append(temp)

blank_list = []
# 빈칸 좌표 전부 저장
for i in range(N):
    for j in range(M):
        if data[i][j] == 0:
            blank_list.append((i, j))

# 벽 3개 좌표 뽑는 경우의 수
candidates = list(combinations(blank_list, 3))

# 바이러스가 퍼진 후의 맵 구하기
def BFS(new_wall_map):
    queue = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 바이러스 좌표(시작좌표) 구해서 큐에 넣기
    for i in range(N):
        for j in range(M):
            if new_wall_map[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        # 상하좌우 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵 벗어나면 무시
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            # 이미 바이러스가 있거나 벽이면 무시
            if new_wall_map[nx][ny] == 2 or new_wall_map[nx][ny] == 1:
                continue
            # 미감염 지역 감염 처리 및 큐에 삽입
            if new_wall_map[nx][ny] == 0:
                new_wall_map[nx][ny] = 2
                queue.append((nx, ny))

    return new_wall_map

# 벽 세울 곳 좌표 전달받고, 시뮬레이션해서 안전 영역의 크기 계산
def simulation(candidate):
    new_wall_map = copy.deepcopy(data)
    # 벽 세우기
    for index in candidate:
        x, y = index
        new_wall_map[x][y] = 1
        
    # 바이러스가 퍼진 후의 맵 구하기 (BFS)
    virus_map = BFS(new_wall_map)
    # 안전영역 개수 세서 반환
    count = 0
    for i in range(N):
        for j in range(M):
            if virus_map[i][j] == 0:
                count += 1
    return count

result = 0
# 벽 세울 후보지 전달
for candidate in candidates:
    result = max(result, simulation(candidate))
print(result)
