# 이진 검색 트리 구현

from __future__ import annotations
from typing import Any, Type

class Node:
    # 이진 검색 트리의 노드
    def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None):
        # 생성자 constructor
        self.key = key
        self.value = value
        self.left = left # 왼쪽 오른쪽 포인터
        self.right = right


class BinarySearchTree:
    # 이진 검색 트리

    def __init__(self):
        # 초기화
        self.root = None # 루트

    def search(self, key: Any) -> Any:
        # 키가 key인 노드를 검색
        p = self.root
        while True:
            if p is None: # 더 이상 진행할 수 없으면
                return None # 검색 실패
            if key == p.key:
                return p.value
            elif key < p.key: # p보다 key값이 작으면..
                p = p.left
            else:
                p = p.right

    def add(self, key: Any, value: Any) -> bool:
        # 키가 key 이고 값이 value인 노드 삽입하기

        def add_node(node: Node, key: Any, value: Any) -> None:
            # node를 루트로 하는 서브트리에 키가 key 이고 값이 value 인 노드 삽입
            if key == node.key:
                return False
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True
        
        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)

    def remove(self, key: Any) -> bool:
        # 키가 key 인 노드 삭제
        p = self.root
        parent = None
        is_left_child = True # p는 parent의 왼쪽 자식 노드인가?

        while True: # 삭제할 키 검색하기
            if p is None:
                return False

            if key == p.key:
                break
            else:
                parent = p
                if key < p.key: # key 쪽이 작으면
                    is_left_child = True # 왼쪽 자식으로 내려간다
                    p = p.left 
                else:
                    is_left_child = False
                    p = p.right

        if p.left is None: # p에 왼쪽 자식이 없으면
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right # 부모의 왼쪽 포인터가 오른쪽 자식을 가리킴
            else:
                parent.right = p.right
        elif p.right is None: # p에 오른쪽 자식이 없으면
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left
            else:
                parent.right = p.left
        else: # 왼쪽 오른쪽 둘 다 있으면
            parent = p
            left = p.left
            is_left_child = True
            while left.right is not None: # 가장 큰 노드 left 검색
                parent = left
                left = left.right
                is_left_child = False

            p.key = left.key
            p.value = left.value
            if is_left_child:
                parent.left = left.left
            else:
                parent.right = left.left
        return True

    def dump(self, reverse: False) -> None:
        # 덤프 (오름차순 출력)

        def print_subtree(node: Node):
            # node를 루트로 하는 서브트리의 노드를 키의 오름차순으로 출력
            if node is not None:
                print_subtree(node.left)
                print(f"{node.key} {node.value}")
                print_subtree(node.right)
        
        def print_subtree_rev(node: Node):
            # 내림차순 출력
            if node is not None:
                print_subtree_rev(node.right)
                print(f"{node.key} {node.value}")
                print_subtree_rev(node.left)

        if reverse:
            print_subtree_rev(self.root)
        else:
            print_subtree(self.root)



