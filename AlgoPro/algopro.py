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

from collection import defaultdict

#Lesson 2
#Ransom Note
class Solution(object):
    def canSpell(self, magazine, note):
        letters = defaultdict(int)
        #for each char at magazine[index], add 1 to corresponding alphabet in letters
        for c in magazine:
            letters[c] += 1

        for c in note:
            if letters[c] <= 0:
                return False
            #decrement from note, on assumption we need to see duplicate letters in magazine
            letters[c] -= 1

        return True

# Ex. input
# where, [] is an array of char defining what is available, and second parameter asking what word can be spelled
# shud be True
print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'bed'))

#Lesson 3
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #iteratively
    def addTwoNumbers(self, l1, l2):
        return self.addTwoNumbersIterative(l1, l2)

    def addTwoNumbersIterative(self, l1, l2):   
        a = l1 
        b = l2
        c = 0
        ret = current = None

        #loop though while either list has a value
        while a or b:
            val = a.val + b.val + c
            c = val / 10
            if not current:
                ret = current = Node(val % 10)
            else:
                current.next = Node(val % 10)
                current = current.next
            if a.next or b.next:
                if not a.next:
                    a.next = Node(0)
                if not b.next:
                    b.next = Node(0)
            a = a.next
            b = b.next
        return ret