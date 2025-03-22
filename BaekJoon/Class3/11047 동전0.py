import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = [int(input().strip()) for _ in range(N)]

coins.reverse()
print(coins)

count = 0
for coin in coins:
    while K >= coin:
        K -= coin
        count += 1

print(count)