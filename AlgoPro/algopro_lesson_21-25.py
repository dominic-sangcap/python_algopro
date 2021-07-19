#lesson 21
#Valid parethenses
class Solution(object):
    def isValid(self, s):
        #map to parethenes pair
        parens = {
            '[' : ']',
            '{' : '}',
            '(' : ')',
        }
        #map inverted of above map
        inv_parens = {v:k for k, v in parens.items()}
        stack = []
        for c in s:
            if c in parens:
                stack.append(c)
            elif c in inv_parens:
                if len(stack) == 0 or stack[-1] != inv_parens[c]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0

#test input
print(Solution().isValid('(){([])}'))
print(Solution().isValid('(){(['))

#Lesson 22
#Find kth largest

#built in sorting algorithm w/ python
def findKthLargest(nums, k):
    return sorted(nums)[len(nums) - k]

#heap version
import heapq
def findKthLargest(nums, k):
    return heapq.nlargest(k, nums)[-1]

#quickselect
import random
def findKthLargest(nums, k):
    def select(list, l, r, index):
        if l == r:
            return list[l]

        pivot_index = random.randint(l, r)

        #move pivot to beginning of list
        list[l], list[pivot_index] = list[pivot_index], list[l]

        #partition
        i = l
        for j in range(l + 1, r + 1):
            if list[j] < list[l]:
                i+=1
                list[i], list[j] = list[j], list[i]

        #move pivot to correct location
        list[i], list[l] = list[l], list[i]

        #recursive partition one side
        if index == i:
            return list[i]
        elif index < i:
            return select(list, l, i - 1, index)
        else:
            return select(list, i + 1, r, index)

    return select(nums, 0, len(nums) - 1, len(nums) - k)


#test input
print(findKthLargest([3, 5, 2, 4, 6, 8], 4))

#lesson 23
#3sum
class Solution:
    def threeSumBruteForce(self, nums):
        result = []
        for i1 in range(0, len(nums)):
            for i2 in range(i1+1, len(nums)):
                for i3 in range(i2+1, len(nums)):
                    a, b, c = nums[i1], nums[i2], nums[i3]
                    if a + b + c == 0:
                        result.append([a, b, c])
        return result

    def threeSumHashmap(self, nums):
        #nums.sort is different from nums.sort() ******
        nums.sort()
        result = []
        for i in range(len(nums)):
            self.twoSumHashmap(nums, i, result)
        return result
    
    def twoSumHashmap(self, nums, start, result):
        values = {}
        target = -nums[start]
        for i in range(start+1, len(nums)):
            n = nums[i]
            diff = target - n
            if diff in values:
                result.append([n, diff, nums[start]])
            values[n] = 1
    
    def threeSumIndices(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums)):
            self.twoSumIndices(nums, i, result)
        return result

    def twoSumIndices(self, nums, start, result):
        low = start + 1
        high = len(nums) - 1
        while low < high:
            sum = nums[start] + nums[low] +nums[high]
            if sum == 0:
                result.append([nums[start], nums[low], nums[high]])
                low += 1
                high -= 1
            elif sum < 0:
                low += 1
            else:
                high -= 1


#test input
print(Solution().threeSumBruteForce([-1, 0, 1, 2, -4, -3]))
print(Solution().threeSumHashmap([-1, 0, 1, 2, -4, -3]))
print(Solution().threeSumIndices([-1, 0, 1, 2, -4, -3]))