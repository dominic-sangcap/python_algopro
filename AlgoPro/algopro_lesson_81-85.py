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