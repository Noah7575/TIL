N, K = map(int, input().split())

result = 1
temp_N = N
for _ in range(K):
    result *= temp_N
    temp_N -= 1

for i in range(1, K+1):
    result /= i

print(int(result))