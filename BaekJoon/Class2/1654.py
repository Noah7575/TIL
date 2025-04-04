import sys
input = sys.stdin.readline

K, N = map(int, input().split())

# 각 랜선의 길이
data = [int(input()) for _ in range(K)]

start = 1
end = max(data)
result = 0
while start <= end:
    count = 0
    mid = (start + end) // 2

    for d in data:
        count += d // mid

    # N보다 적게 만들었다면 길이를 줄인다
    if count < N:
        end = mid -1
    else:
        start = mid + 1
        result = max(result, mid)

print(result)