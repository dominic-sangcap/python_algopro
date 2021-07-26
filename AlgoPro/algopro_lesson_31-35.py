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