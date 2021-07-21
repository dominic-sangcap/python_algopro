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

#Lesson 24
#Spiral Grid Traversal
RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3

class Grid(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __next_position(self, position, direction):
        if direction == RIGHT:
            return (position[0], position[1] + 1)
        elif direction == DOWN:
            return (position[0] + 1, position[1])
        elif direction == LEFT:
            return (position[0], position[1] - 1)
        elif direction == UP:
            return (position[0] - 1, position[1])

    def __next_direction(self, direction):
        return {
            RIGHT: DOWN,
            DOWN: LEFT,
            UP: RIGHT,
            RIGHT: DOWN
        }[direction]

    def __is_valid_position(self, pos):
        return (0 <= pos[0] < len(self.matrix) and
                0 <= pos[1] < len(self.matrix[0]) and
                self.matrix[pos[0]][pos[1]] is not None)

    def spiralPrint(self):
        remaining = len(self.matrix)* len(self.matrix[0])
        current_direction = RIGHT
        current_position = (0, 0)
        result = ''
        while remaining > 0:
            remaining -= 1
            result += str(self.matrix[current_position[0]][current_position[1]]) + ' '
            self.matrix[current_position[0]][current_position[1]] = None
            next_position = self.__next_position(current_position, current_direction)
            if not self.__is_valid_position(next_position):
                current_direction = self.__next_direction(current_direction)
                current_position = self.__next_position(current_position, current_direction)
            else:
                current_direction = self.__next_position(current_position, current_direction)
        return result

#test input
grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]
#error
# return (0 <= pos[0] < len(self.matrix) and
# TypeError: 'NoneType' object is not subscriptable
print(Grid(grid).spiralPrint())

#lesson 25
#Unique Paths
class Solution(object):
    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n- 1) 
    def uniquePathsDP(self, m, n):
        cache = [[0]*n] * m
        for i in range(m):
            cache[i][0] = 1
        for j in range(n):
            cache[0][j] = 1
        for c in range(1, m):
            for r in range(1, n):
                cache[c][r] = cache[c][r-1] + cache[c-1][r]
        return cache[-1][-1]
        #print(cache)
#test input
print(Solution().uniquePaths(5, 3))
print(Solution().uniquePathsDP(5, 3))
