import sys
from collections import Counter
input = sys.stdin.readline

N = int(input().strip())
data = [int(input().strip()) for _ in range(N)]
data.sort()

# 산술 평균 (반올림)
a = int(sum(data) / N) #정수부
b = (sum(data) / N) - int(sum(data) / N) # 소수부
# 양수인 경우와 음수인 경우 구분
if sum(data) > 0:
    if b >= 0.5:
        a += 1
else: # 음수인 경우
    if b <= -0.5:
        a -= 1
    

print(a)

# 중앙값
if N >= 3:
    idx = (N-1) // 2
    print(data[idx])
else:
    print(data[0])

# 최빈값
if len(data) >= 2:
    cnt_dict = Counter(data).most_common(2)
    # 등장횟수가 같으면 두 번째로 작은 것을 고름
    if cnt_dict[0][1] == cnt_dict[1][1]:
        print(cnt_dict[1][0])
    else:
        print(cnt_dict[0][0])
else:
    print(data[0])

# 범위
wide = max(data) - min(data)
print(wide)