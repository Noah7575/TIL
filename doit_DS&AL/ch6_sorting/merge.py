# 정렬을 마친 두 배열을 병합하기

from typing import Sequence, MutableSequence

def merge_sorted_list(a: Sequence, b: Sequence, c: MutableSequence) -> None:
    # 정렬을 마친 배열 a와 b를 병합하여 c에 저장
    pa, pb, pc = 0, 0, 0
    na, nb, nc = len(a), len(b), len(c)

    while pa < na and pb < nb:
        # pa와 pb 중 작은 값을 pc에 저장한다
        if a[pa] <= b[pb]:
            c[pc] = a[pa]
            pa += 1
        else:
            c[pc] = b[pb]
            pb += 1

    while pa < na:
        # a에 남는 원소를 C에 복사
        c[pc] = a[pa]
        pa += 1
        pc += 1

    while pb < nb:
        c[pc] = b[pb]
        pb += 1
        pc += 1