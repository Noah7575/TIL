def med3(a, b, c):
    if a >= b : 
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b
    
a = int(input())
b = int(input())
c = int(input())

print(f"중앙값: {med3(a, b, c)}")