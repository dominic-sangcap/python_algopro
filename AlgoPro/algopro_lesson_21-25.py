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