from itertools import combinations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []
distances = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            houses.append((i, j))
        elif graph[i][j] == 2:
            chickens.append((i, j))

candidates = list(combinations(chickens, M))

def chicken_dist(group):
    result = 0
    # 집 별 치킨 거리를 구해서 더한다
    for house in houses:
        # 가장 가까운 집-치킨거리
        dist = 999
        for chicken in group:
            temp = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
            dist = min(dist, temp)
        result += dist
    return result

for group in candidates:
    distances.append(chicken_dist(group))

print(min(distances))
        