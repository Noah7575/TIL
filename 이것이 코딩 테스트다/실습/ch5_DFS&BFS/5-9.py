from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐 구현을 위해 덱 라이브러리 사용
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나 뽑아 출력
        v = queue.popleft()
        print(v, end = " ")
        # 해당 원소와 연결된, 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 노드 연결 정보 - 2차원 리스트 자료형으로 표현
graph = [
    [], #0
    [2, 3, 8], #1
    [1, 7], #2
    [1, 4, 5], #3
    [3, 5], #4
    [3, 4], #5
    [7], #6
    [2, 6, 8], #7
    [1, 7] #8
]

# 각 노드가 방문한 정보
visited = [False] * 9

bfs(graph, 1, visited)