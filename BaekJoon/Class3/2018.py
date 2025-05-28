# 수들의 합 5
import sys
input = sys.stdin.readline

N = int(input().strip())

# 슬라이딩 윈도우
left = 1
total = 0
count = 0
target = N

for right in range(1, N+1):
    total += right
    while total > target:
        total -= left
        left += 1
    if total == target:
        count += 1

print(count)


