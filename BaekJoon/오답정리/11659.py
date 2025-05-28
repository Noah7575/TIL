# 구간합 구하기 4

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
prefix = list(map(int, input().split()))
# 사전합
for i in range(N-1):
    prefix[i+1] += prefix[i]

for _ in range(M):
    a, b = map(int, input().split())
    # 좌표처리(0시작)
    a -= 1
    b -= 1
    # 구간합 출력
    # 예외처리
    if a == 0:
        print(prefix[b])
    else:
        print(prefix[b] - prefix[a-1])
