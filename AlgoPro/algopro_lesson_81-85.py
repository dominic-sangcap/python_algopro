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