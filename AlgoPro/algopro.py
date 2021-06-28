#Lesson 1
#declare node
class Node(object):
    def __init__(self, val, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

class Solution(object):
    def _isValidBSTHelper(self, n, low, high):
        if not n:
            return True
        val = n.val
        if ((val > low and val < high) and 
            self._isValidBSTHelper(n.left, low, n.val) and 
            self._isValidBSTHelper(n.right, n.val, high)):
            return True
        return False

    def isValidBST(self, n):
        return self._isValidBSTHelper(n, float('-inf'), float('inf'))

# Ex. input


#Lesson 2