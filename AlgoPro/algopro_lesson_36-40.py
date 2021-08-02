#Lesson 36
#All Values At Height
class Node():
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def valuesAtLevel(node, depth):
    if not node:
        return[]

    if depth == 1:
        return [node.value]
    
    return valuesAtLevel(node.left, depth - 1) + valuesAtLevel(node.right, depth - 1)

#test input
node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.right.right = Node(7)
node.left.left = Node(4)
node.left.right = Node(5)

print(valuesAtLevel(node, 3))
print(valuesAtLevel(node, 2))
print(valuesAtLevel(node, 1))

#Lesson 37
#balanced binary tree
class Node(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    #returns True/False, and depth of node
    def _is_balanced_helper(self, n):
        if not n:
            return (True, 0)
        
        lBalanced, lHeight = self._is_balanced_helper(n.left)
        rBalanced, rHeight = self._is_balanced_helper(n.right)
        return (lBalanced and rBalanced and abs(lHeight - rHeight) <= 1, 
            max(lHeight, rHeight) + 1)


    def isBalanced(self, n):
        return self._is_balanced_helper(n)[0]

#test input
n = Node(1)
n.left = Node(2)
n.left.left = Node(4)
n.right = Node(3)
print(Solution().isBalanced(n))

n.right = None
print(Solution().isBalanced(n))

#Lesson 38
#Count of Unival Subtrees
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def count_unival_subtrees(node):
    count, is_unival = count_unival_subtrees_helper(node)
    return count

def count_unival_subtrees_helper(node):
    if not node:
        return 0, True
    
    left_count, is_left_unival = count_unival_subtrees_helper(node.left)
    right_count, is_right_unival = count_unival_subtrees_helper(node.right)

    if is_left_unival and is_right_unival and (not node.left or node.val == node.left.val) and (not node.right or node.val == node.right.val):
        return left_count + right_count + 1, True
    
    return left_count + right_count, False

#test input
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1
a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)

print(count_unival_subtrees(a))