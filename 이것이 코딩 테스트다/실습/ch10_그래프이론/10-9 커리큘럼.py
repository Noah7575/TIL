from collections import deque
import copy

# 노드의 개수 입력받기
v = int(input())
indegree = [0] * (v + 1)
graph = [
    [] for i in range(v + 1)
]
time = [0] * (v + 1)

# 방향 그래프의 모든 간선 정보 입력받기
for i in range(1, v + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    