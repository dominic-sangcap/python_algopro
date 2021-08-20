#Lesson 56
#Level by Level Trees
from collections import deque

class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = []

def levelPrint(node):
    q = deque([node])
    result = ''
    while len(q):
        num = len(q)
        while num > 0:
            node = q.popleft()
            num -= 1
            result += str(node.val)
            for child in node.children:
                q.append(child)
        result += "\n"
    return result

#test input
tree = Node('a', [])
tree.children = [Node('b', []), Node('c', [])]
tree.children[0].children = [Node('g', [])]
tree.children[1].children = [Node('d', []), Node('e', []), Node('f', [])]

print(levelPrint(tree))