import sys
input = sys.stdin.readline
# input 함수할당

N = int(input())
numbers = list(int(input().split()))

cnt = 0
index = 0
# 소수면 1, 아니면 0

for i in range(N):
    # i번째 숫자에 대해 소수 판정
    # 소수인 걸 발견한 경우 index를 1로 만들고 break
    for j in range(2, numbers[i]):
        if numbers[i] 