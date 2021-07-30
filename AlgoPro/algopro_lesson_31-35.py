#Lesson 31
#Intersection of 2 Linked Lists
class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Solution(object):
    def _length(self, n):
        len = 0
        curr = n
        while curr:
            curr = curr.next
            len+=1
        return len

    def intersection(self, a, b):
        lenA = self._length(a)
        lenB = self._length(b)
        currA = a
        currB = b
        if lenA > lenB:
            for _ in range(lenA - lenB):
                currA = currA.next
        else:
            for _ in range(lenB - lenA):
                currB = currB.next

        while currA != currB:
            currA = currA.next
            currB = currB.next

        return currA

#test input
a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next

print(Solution().intersection(a, b).value)

#Lesson 32
#First missing pos integer
class Solution(object):
    def first_missing_position(self, nums):
        hash = {}
        for n in nums:
            hash[n] = 1

        for i in range(1, len(nums)):
            if i not in hash:
                return i
        return -1
#test input
print(Solution().first_missing_position([3, 4, -1, 1]))

#Lesson 33
#Meeting Rooms
import heapq

def meeting_rooms(meetings):
    meetings.sort(key=lambda x: x[0])
    meeting_ends = []
    max_rooms = 0

    for meeting in meetings:
        while meeting_ends and meeting_ends[0] <= meeting[0]:
            heapq.heappop(meeting_ends)
        heapq.heappush(meeting_ends, meeting[1])
        max_rooms = max(max_rooms, len(meeting_ends))

    return max_rooms
#test input
print(meeting_rooms([[0, 10], [10, 20]]))

print(meeting_rooms([[20, 30], [10, 21], [0, 50]]))

#Lesson 34
#Sort Colors
from collections import defaultdict

class Solution(object):
    #hashmap implementation
    def sortColors(self, colors):
        colorsMap = defaultdict(int)
        for c in colors:
            colorsMap[c] += 1

        index = 0
        for i in range(colorsMap[0]):
            colors[index] = 0
            index += 1
        for i in range(colorsMap[1]):
            colors[index] = 1
            index += 1
        for i in range(colorsMap[2]):
            colors[index] = 2
            index += 1

    #indeces sort
    def sortColors2(self, colors):
        lowIndex = 0
        highIndex = len(colors) - 1
        currIndex = 0

        while currIndex <= highIndex:
            if colors[currIndex] == 0:
                colors[lowIndex], colors[currIndex] = colors[currIndex], colors[lowIndex]
                lowIndex += 1
                currIndex += 1
            elif colors[currIndex] == 2:
                colors[highIndex], colors[currIndex] = colors[currIndex], colors[highIndex]
                highIndex -= 1
            else:
                currIndex += 1

#test input
colors = [0, 2, 1, 0, 1, 1, 2]
Solution().sortColors(colors)
print(colors)

colors = [0, 2, 1, 0, 1, 1, 2]
Solution().sortColors2(colors)
print(colors)

#Lesson 35
#Number of Islands
class Solution(object):
    def num_islands(self, grid):
        if not grid or not grid[0]:
            return 0
        numRows, numCols = len(grid), len(grid[0])
        count = 0

        for row in range(numRows):
            for col in range(numCols):
                if self._is_land(grid, row, col):
                    count += 1
                    self._sinkLand(grid, row, col)
        return count
    
    def _sinkLand(self, grid, row, col):
        if not self._is_land(grid, row, col):
            return 
        grid[row][col] = 0
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            self._sinkLand(grid, row + d[0], col + d[1])

    def _is_land(self, grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return False
        return grid[row][col] == 1
    
#test input
grid = [[1, 1, 0, 0, 0], 
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1], 
        [0, 0, 0, 0, 0]]

print(Solution().num_islands(grid))