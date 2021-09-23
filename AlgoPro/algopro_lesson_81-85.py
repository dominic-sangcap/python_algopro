#Lesson 81
#Swap every two nodes
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def __repr__(self):
    return f"{self.value}, ({self.next.__repr__()})"


def swap_every_two(node):
  curr = node
  while curr != None and curr.next != None:
    curr.value, curr.next.value = curr.next.value, curr.value
    curr = curr.next.next
  return node

#test input
node = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(swap_every_two(node))

#lesson 82
#multitasking
def findtime(tasks, cooldown):
  lastpos = {}
  current = 0

  for task in tasks:
    if task in lastpos:
      if current - lastpos[task] <= cooldown:
        current = cooldown + lastpos[task] + 1
    lastpos[task] = current
    current += 1
    print(lastpos)
  return current

#test input
print(findtime([1, 1, 2, 1], 2))

#Lesson 83
#generate binary search trees
class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __repr__(self):
    result = str(self.value)
    if self.left:
      result = result + str(self.left)
    if self.right:
      result = result + str(self.right)
    return result

def gen_tree(nums):
  if len(nums) == 0:
    return [ None ]
  if len(nums) == 1:
    return [ Node(nums[0]) ]

  bsts = []
  for n in nums:
    lefts = gen_tree(range(nums[0], n))
    rights = gen_tree(range(n + 1, nums[-1] + 1))

    for left in lefts:
      for right in rights:
        tree = Node(n, left, right)
        bsts.append(tree)

  return bsts

def generate_bst(n):
  return gen_tree(range(1, n + 1))

#test input
print(generate_bst(3))

#Lesson 84
#zig zag binary trees
class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right


def zigzag_order(node):
  result = []
  currLevel = [node]
  nextLevel = []
  leftToRight = False

  while len(currLevel) > 0:
    node = currLevel.pop()
    result.append(node.value)

    if leftToRight:
      if node.left:
        nextLevel.append(node.left)
      if node.right:
        nextLevel.append(node.right)
    if leftToRight != True:
      if node.right:
        nextLevel.append(node.right)
      if node.left:
        nextLevel.append(node.left)

    if len(currLevel) == 0:
      leftToRight = not leftToRight
      currLevel = nextLevel
      nextLevel = []

  return result

#test input
n7 = Node(7)
n6 = Node(6)
n5 = Node(5)
n4 = Node(4)
n3 = Node(3, n6, n7)
n2 = Node(2, n4, n5)
n1 = Node(1, n2, n3)

print(zigzag_order(n1))

#Lesson 85
#balanced binary trees
class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right


def tree_height(node):
  if node is None:
    return 0

  heightLeft = tree_height(node.left)
  heightRight = tree_height(node.right)

  if heightLeft >= 0 and heightRight >= 0 and abs(heightLeft - heightRight) <= 1:
    return max(heightLeft, heightRight) + 1
  return -1


def is_tree_balanced(node):
  return tree_height(node) != -1

#teset input
n4 = Node(4)
n3 = Node(3)
n2 = Node(2, n4)
n1 = Node(1, n2, n3)

#      1
#     / \
#    2   3
#   /
#  4
print(is_tree_balanced(n1))
# True

n4 = Node(4)
n2 = Node(2, n4)
n1 = Node(1, n2, None)

#      1
#     /
#    2
#   /
#  4
print(is_tree_balanced(n1))
# False