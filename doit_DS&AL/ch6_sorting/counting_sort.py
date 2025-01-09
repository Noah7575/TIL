# 도수 정렬 알고리즘 구현

from typing import MutableSequence

def fsort(a: MutableSequence, max: int) -> None:
    # 도수 정렬
    n = len(a)
    f = [0] * (ma)
    b = [0] * n 

    for i in range(n):
        f[a[i]] += 1
    for i in range(1, max + 1):
        f[i] += f[i - 1]
    for i in range(n - 1, -1, -1):
        f[a[i]] -= 1
        b[f[a[i]]] = a[i]
    for i in range(n):
        a[i] = b[i]

def counting_sort(a: MutableSequence) -> None:
    # 도수 정렬
    fsort(a, max(a))
    