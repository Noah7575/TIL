import sys
from itertools import combinations

N, M = map(int, input().split())
datas = map(int, input().split())

combs = list(combinations(datas, 3))

sum_max = 0
for comb in combs:
    # 경우의 수 합 구하기
    temp = sum(comb)
    
    if temp <= M:
        sum_max = max(temp, sum_max)

print(sum_max)