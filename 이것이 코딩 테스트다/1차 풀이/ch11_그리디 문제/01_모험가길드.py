import sys
input = sys.stdin.readline

n = int(input().strip())
data = list(map(int, input().split()))
data.sort(reverse = True)

result = 0
count = 0 # 모험가의 수

for i in data:
    count += 1 # 현재 그룹에 모험가 포함
    if count >= i:
        result += 1 # 총그룹수 1 증가
        count = 0 # 초기화

print(result)






