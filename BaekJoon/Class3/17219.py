import sys
input = sys.stdin.readline

N, M = map(int, input().split())

info = dict()
for _ in range(N):
    site, pw = input().split()
    info[site] = pw

for _ in range(M):
    q = input().strip()
    print(info[q])