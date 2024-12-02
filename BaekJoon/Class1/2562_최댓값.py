import sys

numbers = [] # 값들 저장

for i in range(9):
    a = int(sys.stdin.readline().strip())
    numbers.append(a)

max_num = 0

for i in range(9):
    if max_num <= numbers[i]:
        max_num = numbers[i]
    else : pass

print(max_num)
print(numbers.index(max_num) + 1)
