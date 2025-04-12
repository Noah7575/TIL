import sys

input = sys.stdin.readline

N, M = map(int, input().split())

data = [[] for _ in range(N+1)]
# 맵 입력받기
for _ in range(M):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

count = 0
visited = [False] * (N+1)
def DFS(start):
    stack = [start]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            for u in data[v]:
                if not visited[u]:
                    stack.append(u)
    global count
    count += 1

for i in range(1, N+1):
    if not visited[i]:
        DFS(i)

print(count)
