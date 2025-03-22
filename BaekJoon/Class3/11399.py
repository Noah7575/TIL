import sys
input = sys.stdin.readline

N = int(input().strip())
P = [int(i) for i in input().split()]

P.sort()

P_add = [0] * N
for i in range(N):
    for j in range(i+1):
        P_add[i] += P[j]

print(sum(P_add))