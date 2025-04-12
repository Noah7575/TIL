import sys
import heapq
input = sys.stdin.readline

heap = []
N = int(input().strip())

for _ in range(N):
    x = int(input().strip())

    # x가 자연수인 경우 힙에 넣는다
    if x >= 1:
        heapq.heappush(heap, x)
    elif x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)

            