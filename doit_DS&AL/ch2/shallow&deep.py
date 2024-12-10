import copy

# shallow copy
x = [[1, 2, 3], [4, 5, 6]]
y = x.copy()

x[0][1] = 9
print(x)
print(y)

# deep copy
x = [[1, 2, 3], [4, 5, 6]]
y = copy.deepcopy(x)

x[0][1] = 9
print(x)
print(y)