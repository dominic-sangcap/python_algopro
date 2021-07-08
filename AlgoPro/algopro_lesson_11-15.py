#Lesson 11
#Max In stack
class MaxStack(object):
    def __init__(self):
        self.stack = []
        self.maxes = []

    def push(self, val):
        self.stack.append(val)
        if self.maxes and self.maxes[-1] > val:
            self.maxes.append(self.maxes[-1])
        else:
            self.maxes.append(val)  

    def pop(self):
        if self.maxes:
            self.maxes.pop()
        return self.stack.pop()


    def max(self):
        return self.maxes[-1]

#test input
s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.pop())
print('max', s.max())
print(s.pop())
print('max', s.max())
print(s.pop())
print('max', s.max())
print(s.pop())

#Lesson 12
#Course Schedule
class Solution:
    def _hasCycle(self, graph, course, seen, cache):
        if course in cache:
            return cache[course]

        if course in seen:
            return True
        if course not in graph:
            return False

        seen.add(course)
        ret = False
        for neighbors in graph[course]:
            if self._hasCycle(graph, neighbors, seen, cache):
                ret = True
        seen.remove(course)

        cache[course] = ret
        return ret

    def canFinish(self, numCourses, prerequistes):
        graph = {}
        #hashmap with arrays as the values
        for prereq in prerequistes:
            print(prereq)
            if prereq[0] in graph:
                graph[prereq[0]].append(prereq[1])
            else:
                graph[prereq[0]] = [prereq[1]]
        
        for course in range(numCourses):
            if self._hasCycle(graph, course, set(), {}):
                return False

        return True
#test input
print(Solution().canFinish(2, [[1, 0]]))
print(Solution().canFinish(2, [[1, 0], [0, 1]]))

#Lesson 13
#Find Pythagorean Triplets
#brute force algorithm
def findPythagTriplets(nums):
    for a in nums:
        for b in nums:
            for c  in nums:
                if a*a + b*b == c*c:
                    return True
    return False
#hashmap variation
def findPythagTriplets2(nums):
    squares = set([n*n for n in nums])

    for a in nums:
        for b in nums:
            if a*a + b*b in squares:
                    return True
    return False
#test input
print(findPythagTriplets([3, 5, 12, 5, 13]))
print(findPythagTriplets2([3, 5, 12, 5, 13]))


