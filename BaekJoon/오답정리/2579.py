import sys
input = sys.stdin.readline

N = int(input().strip())
stairs = []
for _ in range(N):
    stairs.append(int(input().strip()))

for i in range(2, N):
    

print(stairs)