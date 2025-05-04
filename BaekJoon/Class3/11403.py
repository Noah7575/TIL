import sys
input = sys.stdin.readline

N = int(input().strip())

INF = int(10e9)
graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    temp = list(map(int, input().split()))
    for j in range(1, N+1):
        if temp[j-1] != 0:
            graph[i][j] = temp[j-1]
        else:
            graph[i][j] = INF

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == INF:
            print(0, end = " ")
        else:
            print(1, end = " ")
    print()

