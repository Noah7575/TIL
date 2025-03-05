from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

graph = [
    [] for _ in range(N + 1)
]

dist = [0] * (N + 1)

# 그래프 정보 입력받기
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(graph, start):
    # 큐
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                dist[i] = dist[v] + 1

visited = [False] * (N+1)

bfs(graph, X)

# 결과 출력
for i in range(N+1):
    if dist[i] == K:
        print(i)

if K not in dist:
    print(-1)

