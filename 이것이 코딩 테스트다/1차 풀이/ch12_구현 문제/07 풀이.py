import sys
input = sys.stdin.readline

N = str(input().strip())

center_digit = int(len(N) / 2)

left_result = 0
right_result = 0

for i in range(0, center_digit):
    left_result += int(N[i])

for i in range(center_digit, len(N)):
    right_result += int(N[i])

if left_result == right_result:
    print("LUCKY")
else:
    print("READY")
