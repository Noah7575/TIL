import sys
import heapq
input = sys.stdin.readline

N = int(input().strip())

heap = []
for _ in range(N):
    x = int(input().strip())

    if x > 0:
        heapq.heappush(heap, -x)
    elif heap:
        a = heapq.heappop(heap)
        print(-a)
    else:
        print(0)