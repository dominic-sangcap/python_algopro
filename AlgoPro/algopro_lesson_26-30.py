#lesson 26
#Stack Queue
class Queue(object):
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def enqueue(self, val):
        self.s1.append(val)

    def dequeue(self):
        if self.s2:
            return self.s2.pop()
        
        if self.s1:
            while self.s1:
                self.s2.append(self.s1.pop())
            return self.s2.pop()
        return None

#test input
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

#Lesson 27
#Remove Zero Sum NOdes
import collections

class Node(object):
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __repr__(self):
        n = self
        ret = ''
        while n:
            ret += str(n.val) + ' '
            n = n.next
        return ret

class Solution(object):
    def removeZeroSumSublists(self, node):
        sumToNode = collections.OrderedDict()
        sum = 0
        dummy = Node(0)
        dummy.next = node
        n = dummy
        while n:
            sum += n.val   
            if sum not in sumToNode:
                sumToNode[sum] = n
            else:
                prev = sumToNode[sum]
                prev.next = n.next
                while list(sumToNode.keys())[-1] != sum:
                    sumToNode.popitem()
            n = n.next           
        return dummy.next

# File "c:\Users\Dom\Desktop\python_algopro\AlgoPro\tempCodeRunnerFile.py", line 30, in removeZeroSumSublists
#     while sumToNode.keys()[-1] != sum:
# TypeError: 'odict_keys' object is not subscriptable
# -----means turn object into a list
#test input
n = Node(3)
n.next = Node(1)
n.next.next = Node(2)
n.next.next.next = Node(-1)
n.next.next.next.next = Node(-2)
n.next.next.next.next.next = Node(4)
n.next.next.next.next.next.next = Node(1)
print(Solution().removeZeroSumSublists(n))
