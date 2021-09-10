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

#lesson 73
#remove duplicate from linked list
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def __repr__(self):
    return f"({self.value}, {self.next})"

def remove_duplicates(node):
  curr = node

  while curr and curr.next:
    if curr.value == curr.next.value:
      curr.next = curr.next.next
    else:
      curr = curr.next
  
#test input
node = Node(1, Node(2, Node(2, Node(3, Node(3)))))
remove_duplicates(node)
print(node)


#Lesson 74
class ListFastSum(object):
  def __init__(self, nums):
    self.pre = [0]

    sum = 0
    for num in nums:
      sum += num
      self.pre.append(sum)

  def sum(self, starts, end):
    return self.pre[end] - self.pre[starts]

#test input
print(ListFastSum([1, 2, 3, 4, 5, 6, 7]).sum(2, 5))


#lesson 75
#Sorted square numbers
def square_numbers(nums):
  neg_i = -1
  i = 0

  result = []
  for n in nums:
    if n >= 0:
      if neg_i == -1:
        neg_i = i - 1

      while neg_i >= 0 and nums[neg_i] < 0 and -nums[neg_i] < nums[i]:
        val = nums[neg_i]
        result.append(val * val)
        neg_i -= 1

      val = nums[i]
      result.append(val * val)
    i += 1

  while neg_i >= 0 and nums[neg_i] < 0:
    val = nums[neg_i]
    result.append(val * val)
    neg_i -= 1

  return result

def square_numbers2(nums):
  result = []
  front = 0
  back = -1

  while nums[back] > nums[front]:
    if abs(nums[front]) > nums[back]:
      result.insert(0, nums[front]**2)
      #print(nums[front]**2, 'front')
      front += 1
    else:
      result.insert(0, nums[back]**2)
      #print(nums[back]**2, 'back')
      back -= 1

  result.insert(0, nums[front]**2)
  
  return result

#test input
print(square_numbers2([-5, -3, -1, 0, 1, 4, 5]))
print(square_numbers([-5, -3, -1, 0, 1, 4, 5]))
