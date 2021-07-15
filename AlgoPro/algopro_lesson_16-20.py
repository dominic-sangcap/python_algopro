#Lesson 16
#Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums):
        right = [1] * len(nums)
        prod = 1
        for i in range(len(nums) - 2, -1, -1):
            prod *= nums[i + 1]
            right[i] = prod
        prod = 1
        for i in range(1, len(nums)):
            prod *= nums[i-1]
            right[i] *= prod
        return right
#test input
#want [24, 12, 8, 6]
print(Solution().productExceptSelf([1, 2, 3, 4]))

#Lesson 17
#Non Decreasing Array
class Solution(object):
    def checkPossibility(self, nums):
        invalid_index = -1
        for i in range(len(nums) - 1):  
            if nums[i] > nums[i+1]:
                if invalid_index != -1:
                    return False
            invalid_index = i
        if invalid_index != -1:
            return True
        if invalid_index == 0:
            return True
        if invalid_index == len(nums) - 2:
            return True
        if nums[invalid_index] <= nums[invalid_index + 2]:
            return True
        if nums[invalid_index - 1] <= nums[invalid_index + 1]:
            return True
        return False
#test input
#[4, 1, 2]
#[3, 2, 4, 1]
print(Solution().checkPossibility([4, 1, 2]))
print(Solution().checkPossibility([3, 2, 4, 1]))

#lesson 18
#Word Search
class Grid(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __wordSearchRight(self, index, word):
        for i in range(len(self.matrix[index])):
            if word[i] != self.matrix[index][i]:
                return False
        return True

    def __wordSearchBottom(self, index, word):
        for i in range(len(self.matrix[index])):
            if word[i] != self.matrix[i][index]:
                return False
        return True

    def wordSearch(self, word):
        for i in range(len(self.matrix)):
            if self.__wordSearchRight(i, word):
                return True
        for i in range(len(self.matrix[0])):
            if self.__wordSearchBottom(i, word):
                return True
        return False

#test input
matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']]
print(Grid(matrix).wordSearch('FOAM'))
print(Grid(matrix).wordSearch('MASS'))


#lesson 19
#top k frequent items

import heapq
import collections

class Solution(object):
    def topKFrequent(self, nums, k):
        count = collections.defaultdict(int)
        for n in nums:
            count[n] += 1

        heap = []
        for num, c in count.items():
            #use - since heap store min, store max count as negative number
            heap.append((-c, num))
        heapq.heapify(heap)
        print(heap)

        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
print(Solution().topKFrequent([1,1,1,2,2,3,], 2))

#lesson 20
#Remove kth element from linked list
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
    def __str__(self):
        n = self
        answer = ''
        while n:
            answer += str(n.val)
            n = n.next
        return answer

def remove_kth_element(node, k):
    slow, fast = node, node
    for i in range(k):
        fast = fast.next
    #edge cases
    if not fast:
        return node.next

    prev = None
    while fast:
        prev = slow
        fast = fast.next
        slow = slow.next
    prev.next = slow.next 
    return node 
#test input
head = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
print(head)
#should remove 3
remove_kth_element(head, 3)
print(head)