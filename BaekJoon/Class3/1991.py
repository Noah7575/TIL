import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node 

N = int(input().strip())    
tree = {}

for _ in range(N):
    data, left_node, right_node = input().split()
    if left_node == ".":
        left_node = None
    if right_node == ".":
        right_node = None
    
    tree[data] = Node(data, left_node, right_node)

def preorder(Nodename):
    if Nodename is not None:
        Node = tree[Nodename]
        print(Node.data, end = '')
        preorder(Node.left_node)
        preorder(Node.right_node)    

def inorder(Nodename):
    if Nodename is not None:
        Node = tree[Nodename]
        inorder(Node.left_node)
        print(Node.data, end='')
        inorder(Node.right_node)

def postorder(Nodename):
    if Nodename is not None:
        Node = tree[Nodename]
        postorder(Node.left_node)
        postorder(Node.right_node)
        print(Node.data, end = '')

preorder('A')
print()
inorder('A')
print()
postorder('A')