import sys
input = sys.stdin.readline

temps = list(input().strip())
nums = [] * (len(temps))

for temp in temps:
    nums.append(int(temp))

print(f"nums: {nums}")

result = 0
for num in nums:
    if (result > 1) and (num > 1):
        result = result * num
    else:
        result = result + num

print(result)
