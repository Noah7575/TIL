import math

stack = []
N = int(input().strip())

count_nums = list(str(math.factorial(N)))
count_nums.reverse()

count = 0
for num in count_nums:
    if num == '0':
        count += 1
    else:
        break

print(count)