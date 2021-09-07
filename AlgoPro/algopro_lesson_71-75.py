#Lesson 71
#Inorder Successor
class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f"({self.value}, {self.left}, {self.right}"

def in_order_successor(node):
  if node.right:
    curr = node.right
    while curr.left:
      curr = curr.left
    return curr

  curr = node
  parent = curr.parent
  while parent and parent.left != curr:
    curr = parent
    parent = parent.parent
  return parent 

#test input
tree = Node(4)
tree.left = Node(2)
tree.right = Node(8)
tree.left.parent = tree
tree.right.parent = tree
tree.left.left = Node(1)
tree.left.left.parent = tree.left
tree.right.right = Node(7)
tree.right.right.parent = tree.right
tree.right.left = Node(5)
tree.right.left.parent = tree.right
tree.right.left.right = Node(7)
tree.right.left.right.parent = tree.right.left
tree.right.right = Node(9)
tree.right.right.parent = tree.right
#     4
#    / \
#   2   8
#  /   / \
# 1   5   9
#      \
#       7

print(in_order_successor(tree.right))

print(in_order_successor(tree.left))

print(in_order_successor(tree.right.left.right))


#Lesson 72
#Rotator Linked List
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next= next

  def __repr__(self):
    return f"({self.value}, {self.next})"

def rotate(node, n):
  length = 0
  curr = node
  while curr != None:
    curr = curr.next
    length += 1
  n = n % length

  slow, fast = node, node
  for i in range(n):
    fast = fast.next

  while fast.next != None:
    slow = slow.next
    fast = fast.next
  
  fast.next = node
  head = slow.next
  slow.next = None

  return head

#test input
node = Node(1, Node(2, Node(3, Node(4, Node(5)))))

print(rotate(node, 2))