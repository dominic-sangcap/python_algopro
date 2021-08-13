#Lesson 46
#Angles of a Clock
def calcAngle(h, m):
    hour_angle = (360 / (12 * 60.0)) * (h * 60 + m)
    min_angle = 360 / 60.0 * m
    angle = abs(hour_angle - min_angle)
    angle = min(angle, 360 - angle)
    return angle

#test input 
print(calcAngle(3, 15))
print(calcAngle(3, 00))

#Lesson 47
#climbing stairs
#recursive implementation
def staircase(n):
    if n <= 1:
        return 1
    return staircase(n - 1) + staircase(n - 2)

def staircase2(n):
    prev = 1
    prevprev = 1
    curr = 0
    for i in range(2, n + 1):
        curr = prev + prevprev

        prevprev = prev
        prev = curr
    return curr

#test input
print(staircase2(5))

print(staircase(5))

#Lesson 48
#Tree Serialization
class Node(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        result = ''
        result += str(self.val)
        if self.left:
            result += str(self.left)
        if self.right:
            result += str(self.right)
        return result

def serialize(node):
    if node == None:
        return '#'
    return str(node.val) + ' ' + str(serialize(node.left)) + ' ' + str(serialize(node.right))

def deserialize(str):
    def deserialize_helper(values):
        value = next(values)

        if value == '#':
            return None
        
        node = Node(int(value))
        node.left = deserialize_helper(values)
        node.right = deserialize_helper(values)
        return node

    values = iter(str.split())
    return deserialize_helper(values)
    

#test input
#      1
#     / \
#    3   4
#   / \   \
#  2   5   7
tree = Node(1)
tree.left = Node(3)
tree.right = Node(4)
tree.left.left = Node(2)
tree.left.right = Node(5)
tree.right.right = Node(7)
string = serialize(tree)
print(string)
print(deserialize(string))

#Lesson 49
#Longest Substring without repeating characters
def lengthOfLongestSubstring(str):
    letter_pos = {}
    start = -1
    end = 0
    max_length = 0

    while end < len(str):
        c = str[end]
        if c in letter_pos:
            start = max(start, letter_pos[c])
        max_length = max(max_length, end - start)

        letter_pos[c] = end
        end += 1

    return max_length

#test input
print(lengthOfLongestSubstring('aabcbbeacc'))