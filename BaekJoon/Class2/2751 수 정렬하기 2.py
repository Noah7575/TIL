N = int(input().strip())

nums = []

for _ in range(N):
    nums.append(int(input().strip()))

nums.sort()

for num in nums:
    print(num)