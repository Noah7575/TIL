def find_parents(parent, x):
    if parent[x] != x:
        parent[x] = find_parents(parent, parent[x])
    return parent[x]

def union_parents(parent, a, b):
    a = find_parents(parent, a)
    b = find_parents(parent, b)
    if a < b:
        parent[b] = a
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0

for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()
last = 0

for edge in edges:
    cost, a, b = edge
    if find_parents(parent, a) != find_parents(parent, b):
        union_parents(parent, a, b)
        result += cost
        last = cost

print(result - last)
