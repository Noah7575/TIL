import sys
input = sys.stdin.readline

N = int(input().strip())
scores = list(map(int, input().split()))

M = max(scores)

new_scores = []
for score in scores:
    temp = (score / M) * 100
    new_scores.append(temp)

print(sum(new_scores) / N)