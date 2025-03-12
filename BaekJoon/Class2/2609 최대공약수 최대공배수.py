N, M = map(int, input().split())

# 최대공약수 구하기
min_num = min(N, M)
GCD = 0 # 최대공약수
for i in range(1, min_num + 1):
    if (N % i == 0) and (M % i == 0):
        GCD = i

print(GCD)

# 최소공배수 구하기
max_num = max(N, M)
LCM = 0
for i in range(max_num, N * M + 1):
    if (i % N == 0) and (i % M == 0):
        LCM = i
        break

print(LCM)

