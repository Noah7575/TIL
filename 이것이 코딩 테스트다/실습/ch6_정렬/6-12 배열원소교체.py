n, k = map(int, input().split())
a_array = list(map(int, input().split()))
b_array = list(map(int, input().split()))

a_array.sort()
b_array.sort(reverse = True)

for i in range(k):
    if a_array[i] < b_array[i]:
        a_array[i], b_array[i] = b_array[i], a_array[i]
    else:
        break # 뒤에 볼 필요 X

print(sum(a_array))