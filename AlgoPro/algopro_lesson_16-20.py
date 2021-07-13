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