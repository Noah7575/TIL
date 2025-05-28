# 2003 수들의 합 2

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
total = 0
count = 0

for right in range(N):
    total += arr[right]
    while total > M:
        total -= arr[left]
        left += 1
    if total == M:
        count += 1

print(count)
