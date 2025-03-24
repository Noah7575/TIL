from collections import deque
import sys
input = sys.stdin.readline
queue = deque()

N = int(input().strip())
D = int(input().strip())

# 연결된 그래프
data = [
    [] for _ in range(N+1)
]

for _ in range(D):
    index, con = map(int, input().split())
    data[index].append(con)
    data[con].append(index)

# BFS
visited = [0] * (N+1)
visited[1] = 1
queue.append(1)

while queue:
    v = queue.popleft()
    for i in data[v]:
        # 미감염인 경우
        if visited[i] == 0:
            visited[i] = 1
            queue.append(i)
        elif visited[i] == 1:
            continue

print(visited.count(1) -1)