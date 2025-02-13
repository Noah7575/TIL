import sys
input = sys.stdin.readline

S = list(map(int, input().strip()))

# 나의 풀이
zero_count = 0
one_count = 0

for i in range(1, len(S)):
    if (S[i] != S[i - 1]):
        if (S[i] == 1):
            zero_count += 1
        else:
            one_count += 1

# min 함수로 대체 가능했음!
result = zero_count if (zero_count < one_count) else one_count

print(result)

# 답지 풀이
count0 = 0 # 1을 0으로 바꾸는 경우
count1 = 0 # 0을 1로 바꾸는 경우

if S[0] == 1:
    count0 += 1
else:
    count1 += 1

for i in range(len(S) - 1):
    if S[i] != S[i+1]:
        if S[i + 1] == 1:
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))