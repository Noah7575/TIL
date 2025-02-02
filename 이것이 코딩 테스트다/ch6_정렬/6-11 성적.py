n = int(input())

array = []

for i in range(n):
    add = input().split()
    print(f"add 값: {add}")
    array.append((add[0], int(add[1])))

array = sorted(array, key = lambda grade: grade[1])

for student in array:
    print(student[0], end = ' ')