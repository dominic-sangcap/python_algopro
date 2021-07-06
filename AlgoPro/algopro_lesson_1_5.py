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
#Add two numbers as linked list
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

#Lesson 4
#Two Sum
class Solution(object):
    #brute force solution
    def twoSum(self, nums, target):
        # must enumertae because of python rules?
        for i1, a in enumerate(nums):
            for i2, b in enumerate(nums):
                if a == b: 
                    continue
                if a + b == target:
                    # i1 & i2 give indeces of value, a & b give numerical values
                    return[i1, i2]
        return []
    
    #hashmap solution
    def twoSumHmap(self, nums, target):
        values = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in values:
                return [i, values[diff]]
            values[num] = i
        return []

#test input
print(Solution().twoSumHmap([1, 2, 5, 12], 14))
print(Solution().twoSum([1, 2, 5, 12], 14))

#Lesson 5
#Get Range
class Solution:
    def getRange(self, arr, target):
        first = self.binarySearch(arr, 0, len(arr) - 1, target, True)
        last = self.binarySearch(arr, 0, len(arr) - 1, target, False)
        return [first, last]
    def binarySearch(self, arr, low, high, target, findFirst):
        if high < low:
            return -1
        mid = low + (high - low) / 2
        if findFirst:
            if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
                return mid  
            if target > arr[mid]:
                return self.binarySearch(arr, mid + 1, high, target, findFirst)
            else:
                return self.binarySearch(arr, low, mid - 1, target, findFirst)
        else:
            if (mid == len(arr)-1 or x < arr[mid + 1]) and arr[mid] == x:
                return mid
            elif target < arr[mid]:
                return self.binarySearch(arr, low, mid - 1, target, findFirst)
            else:
                return self.binarySearch(arr, mid + 1, high, target, findFirst)

#Error: TypeError: list indices must be integers or slices, not float
#test input
arr = [1, 3, 3, 5, 7, 8, 9, 9, 15]
x = 9
print(Solution().getRange(arr, x))