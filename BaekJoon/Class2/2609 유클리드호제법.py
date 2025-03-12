# 최대공약수
def GCD(x, y):
    while y:
        x, y = y, x % y
    return x

# 최소공배수
def LCM(x, y):
    result = (x * y) // GCD(x, y)
    return result

print(GCD(24, 18))
print(LCM(24, 18))