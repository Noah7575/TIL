from collections import deque
import sys
input = sys.stdin.readline
queue = deque()

N, K = map(int, input().split())

data = []
for i in range(N):
    temp = list(map(int, input().split()))
    data.append(temp)

S, X, Y = map(int, input().split())

def bfs():
    # 이동 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        vx, vy = queue.popleft()

        # 4방향 점검
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            # 맵을 벗어나면 무시
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            # 빈칸이라면 번식
            if data[nx][ny] == 0:
                data[nx][ny] = data[vx][vy]

# S초 동안의 번식
for _ in range(S):
    # 바이러스 순서대로 큐에 넣는다
    # 이미 돌린 건 제외
    done = []
    for k in range(1, K+1):
        for x in range(N):
            for y in range(N):
                if data[x][y] == k and (x, y) not in done:
                     queue.append((x, y))
                     done.append((x, y))
    bfs()

# 결과 찾기
print(data[X-1][Y-1])