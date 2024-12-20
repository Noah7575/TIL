# 체인법을 구현하는 해시 클래스 chainedhash 사용하기

from enum import Enum
from chained_hash import ChainedHash

Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료'])

def select_menu() -> Menu:
    # 메뉴 선택
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '   ', end='') # sep: 구분자
        n = int(input(": "))
        if 1 <= n <= len(Menu):
            return Menu(n)

hash = ChainedHash(13)
# 크기 13의 해시테이블 생성

while True:
    menu = select_menu() # 메뉴선택

    if menu == Menu.추가:
        key = int(input("추가할 키를 입력하세요.: "))
        val = input("추가할 값을 입력하세요. : ")
        if not hash.add(key, val): # True 가 아니면
            print("추가 실패!")
        
    elif menu == Menu.삭제:
        key = int(input("삭제할 키를 입력하세요. :"))
        if not hash.remove(key):
            print("삭제 실패!")

    elif menu == Menu.검색:
        key = int(input("검색할 키 입력: "))
        t = hash.search(key)
        if t is not None:
            print(f"검색할 키를 갖는 값은 {t}입니다.")
        else:
            print("검색할 데이아가 없습니다.")

    elif menu == Menu.덤프:
        hash.dump()

    else:
        break

