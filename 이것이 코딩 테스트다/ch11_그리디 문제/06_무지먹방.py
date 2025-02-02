import sys 
input = sys.stdin.readline

food_times = list(map(int, input().split()))
K = int(input())
N = len(food_times)

result = 0
for i in range(K):
    while (food_times[result] != 0):
        result += 1
        result %= N
    food_times[result] -= 1


print(result)