from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

def BFS(start, end):
    queue = deque()
    queue.append(start * 2)
    queue.append(start + 1)
    queue.append(start - 1)
    time = [0] * (10 ** 7)
    visited = [False] * (10 ** 7)
    time[start * 2] = 1
    time[start + 1] = 1
    time[start - 1] = 1

    # bfs
    while queue:
        v = queue.popleft()
        if v == end:
            return time[v]
        
        for nx in [v * 2, v - 1, v + 1]:
            if 0 <= nx < (10 ** 7) and not visited[nx]:
                visited[nx] = True
                time[nx] = time[v] + 1

print(BFS(N, K))