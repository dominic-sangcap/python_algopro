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

#Lesson 28
#Merge k sorted lists
class Node(object):
    def __init__(self, val, next =None):
        self.val = val  
        self.next = next
    def __str__(self):
        c = self
        answer = ''
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer

#add all values, sort afterwards
def merge(lists):
    arr = []
    for node in lists:
        while node:
            arr.append(node.val)
            node = node.next
    head = root = None
    for val in sorted(arr):
        if not root:
            head = root = Node(val)
        else:
            root.next = Node(val)
            root = root.next
    return head

def merge2(lists):
    head = current = Node(-1)

    while any(list is not None for list in lists):
        current_min, i = min((list.val, i) for i, list in enumerate(lists) if list is not None)
        lists[i] = lists[i].next
        current.next = Node(current_min)
        current = current.next
    
    return head.next

#test input
a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))

print(a)
# 135
print(b)
# 246
print(merge([a, b]))
print(merge2([a, b]))

#Lesson 29
#generate parenthesis
class Solution(object):
    def _genParensHelper(self, n, left, right, str):
        if left + right == 2* n:
            return [str]
        
        result = []
        if left < n:
            result += self._genParensHelper(n, left + 1, right, str+'(')
        if right < left:
            result += self._genParensHelper(n, left, right + 1, str+')')
        return result

    def genParens(self, n):
        return self._genParensHelper(n, 0, 0, '')
        return []
        
#test input
print(Solution().genParens(3))