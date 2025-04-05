import sys
input = sys.stdin.readline

N = int(input().strip())
data = [i for i in map(int, input().split())]
M = int(input().strip())

start = 0
end = max(data)
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 0

    for d in data:
        if d <= mid:
            count += d
        else:
            count += mid

    if count > M:
        end = mid - 1
    else:
        start = mid + 1
        result = max(result, mid)

print(result)