import sys
input = sys.stdin.readline

N, K = map(int, input().split())

trees = [i for i in map(int, input().split())]

start = 0
end = max(trees)
result = 0

while start <= end:
    count = 0
    mid = (start + end) // 2

    for tree in trees:
        if tree > mid:
            count += tree - mid

    # 나무가 부족하면 칼 높이를 낮추자
    if count < K:
        end = mid - 1
    else: # 나무가 많다면 높이를 높여보자
        start = mid + 1
        result = max(result, mid)

print(result)