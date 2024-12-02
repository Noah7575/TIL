import sys

N = int(sys.stdin.readline().strip())
numbers = sys.stdin.readline().strip()

result = 0

for i in range(N):
    result = result + int(numbers[i])

print(result)