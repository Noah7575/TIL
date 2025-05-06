import sys
input = sys.stdin.readline

N = int(input().strip())
graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(0, N):
        if j == 0:
            graph[i][j] += graph[i-1][j]
        elif j > i:
            pass
        elif i == j:
            graph[i][j] += graph[i-1][j-1]
        else:
            graph[i][j] += max(graph[i-1][j], graph[i-1][j-1])

print(max(graph[N-1]))