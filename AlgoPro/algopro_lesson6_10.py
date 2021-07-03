#Lesson 6 
#Permutations
class Solution(object):
    def _permuteHelper(self, nums, start = 0):
        if start == len(nums):
            return [nums[:]]
            #what does the [:] mean
        
        result = []

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            result += self._permuteHelper(nums, start + 1)
            nums[start], nums[i] = nums[i], nums[start]
        return result
           
    def permute(self, nums):
        return self._permuteHelper(nums)

    #other way to solve this
    def permute2(self, nums, values=[]):
        if not nums:
            return [values]
        result = []
        for i in range(len(nums)):
            result += self.permute2(nums[:i] + nums[i+1:], values + [nums[i]])
        return result

#test input
print(Solution().permute2([1, 2, 3]))

#Lesson 7
#Sort 3 unique values
def sortNums(nums):
    #hashmap approach
    counts = {}
    for n in nums:
        counts[n] = counts.get(n, 0 ) + 1
    return ([1] * counts.get(1, 0) + 
        [2] * counts.get(2, 0) +
        [3] * counts.get(3, 0))

def sortNums2(nums):
    one_index = 0
    three_index = len(nums) - 1
    index = 0
    while index <= three_index:
        if nums[index] == 1:
            nums[index], nums[one_index] = nums[one_index], nums[index]
            one_index += 1
            index += 1
        if nums[index] == 2:
            index += 1
        if nums[index] == 3:
            nums[index], nums[three_index] = nums[three_index], nums[index]
            three_index -= 1
    return nums

#test input
print(sortNums2([3, 3, 2, 1, 1, 2, 3, 2, 1]))
print(sortNums([3, 3, 2, 1, 1, 2, 3, 2, 1]))