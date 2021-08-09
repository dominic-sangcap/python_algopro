#lesson 41
#Minimum Subarray Length
class Solution(object):
    def minSubArray(self, k, nums):
        leftIndex = rightIndex = 0
        sum = 0
        minLen = float('inf')

        while rightIndex < len(nums):
            sum += nums[rightIndex]
            while sum >= k:
                minLen = min(minLen, rightIndex - leftIndex + 1)
                sum -= nums[leftIndex]
                leftIndex += 1
            rightIndex += 1

        if minLen == float('inf'):
            return 0
        return minLen
#test input
print(Solution().minSubArray(7, [2, 3, 1, 2, 4, 3]))

#Lesson 42
#Merge List of Number Into Ranges
def makeRange(low, high):
    return str(low) + '-' + str(high)

def findRanges(nums):
    if not nums:
        return []

    ranges = []
    low = nums[0]
    high = nums[0]

    for n in nums:
        if high + 1 < n:
            ranges.append(makeRange(low, high))
            low = n
        high = n
    ranges.append(makeRange(low, high))
    return ranges

#test input
print(findRanges([0, 1, 2, 5, 7, 8, 9, 10, 11, 15]))

#Lesson 43
#Max Subarray
class Solution(object):
    def maxSubArray(self, nums):
        maxSum = 0
        sum = 0
        for n in nums:
            sum += n
            if sum < 0: 
                sum = 0
            else:
                maxSum = max(maxSum, sum)
        return maxSum

#test input
print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

#Lesson 44
#Array Intersection
class Solution(object):
    #brute force
    def intersection(self, nums1, nums2):
        results = {}
        for num in nums1:
            if num in nums2 and num not in results:
                results[num] = 1
        return list(results.keys())

    #built in functions, w/ sets
    def intersection2(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        return [x for x in set1 if x in set2]

    #double hashmap implementations
    def intersection3(self, nums1, nums2):
        hash = {}
        duplicates = {}
        for i in nums1:
            hash[i] = 1
        for i in nums2:
            if i in hash:
                duplicates[i] = 1

        #tuple returns (), no tuple returns []
        return tuple(duplicates.keys())

#test input
print(Solution().intersection3([4, 9, 5], [9, 4, 9, 8, 4]))


#Lesson 45
#Invert Binary Tree
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        result = self.val
        result += f"{self.left}" if self.left else ''
        result += f"{self.right}" if self.right else ''
        return result

class Solution(object):
    def invert(self, n):
        if not n:
            return None
        left = self.invert(n.left)
        right = self.invert(n.right)
        n.right = left
        n.left = right
        return n

n = Node('a')
n.left = Node('b')
n.right = Node('c')
n.left.left = Node('d')
n.left.right = Node('e')
n.right.left = Node('f')

#       a
#     /  \
#    b    c
#   / \  /
#  d  e  f

print(n)

#       a
#     /  \
#    c    b
#     \  / \
#     f e   d
print(Solution().invert(n))