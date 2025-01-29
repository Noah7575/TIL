import sys
input = sys.stdin.readline

## 나의 풀이
N, M = map(int, input().split())
K = list(map(int, input().split()))

result = 0

for i in range(N):
    for j in range(i + 1, N):
        if K[i] != K[j]:
            result += 1

print(result)
        
## 답지의 풀이
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1~10 무개별 개수 리스트
array = [0] * 11

for x in data:
    # 무계 해당 개수 카운트
    array[x] += 1

result = 0
# 1~m까지 무게에 대해 처리
for i in range(1, m+1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택 가능한 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱하기

print(result)