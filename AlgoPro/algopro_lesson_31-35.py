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