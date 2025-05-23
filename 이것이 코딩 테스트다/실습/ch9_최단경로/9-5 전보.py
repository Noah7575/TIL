import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    # X노드에서 y노드로 가는 비용이 z
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단경로는 0
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 최단거리 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
        # 현재 노드를 거쳐서 이동하는 거리가 더 짧은 경우
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))
    
dijkstra(start)

# 도달할 수 있는 노드의 개수
count = 0
max_distnace = 0
for d in distance:
    if d != INF:
        count += 1
        max_distnace = max(max_distnace, d)

print(count - 1, max_distnace)

