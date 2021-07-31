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