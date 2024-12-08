# 리스트 원솟값 업데이트

def change(lst, idx, val):
    # list[idx]값을 val로 업데이트
    lst[idx] = val

x = [11, 22, 33, 44, 55]
print("x = ", x)

index = int(input("업데이트할 인덱스: "))
value = int(input("새로운 값: "))

change(x, index, value)
print(f"x = {x}")

"""
인수가 뮤터블인 경우: 함수 안에서 매개변수 값을 변경 시 객체 자체를 업데이트한다
"""