from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
# 그래프 입력받기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs 스택으로 구현하기
def dfs(data, N, start):
    visited = [False] * (N+1)
    stack = [start]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            print(v, end = ' ')
            for u in sorted(graph[v], reverse = True):
                if not visited[u]:
                    stack.append(u)

# bfs
def bfs(data, N, start):
    visited = [False] * (N+1)
    visited[start] = True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for u in sorted(graph[v]):
            if not visited[u]:
                queue.append(u)
                visited[u] = True


dfs(graph, N, V)
print()
bfs(graph, N, V)