#Lesson 56
#Level by Level Trees
from collections import deque

class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = []

def levelPrint(node):
    q = deque([node])
    result = ''
    while len(q):
        num = len(q)
        while num > 0:
            node = q.popleft()
            num -= 1
            result += str(node.val)
            for child in node.children:
                q.append(child)
        result += "\n"
    return result

#test input
tree = Node('a', [])
tree.children = [Node('b', []), Node('c', [])]
tree.children[0].children = [Node('g', [])]
tree.children[1].children = [Node('d', []), Node('e', []), Node('f', [])]

print(levelPrint(tree))

#Lesson 57
#Max connected colors in a grid
class Grid:
    def __init__(self, grid):
        self.grid = grid

    def max_connected_colors(self):
        max_n = 0
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                #max_n = max(max_n, self.dfs(x, y, {}))
                max_n = max(max_n, self.dfsIterative(x, y, {}))
        return max_n

    def colorAt(self, x, y):
        if x >= 0 and x < len(self.grid[0]) and y >= 0 and y < len(self.grid):
            return self.grid[y][x]
        return -1

    def neighbors(self, x, y):
        POSITIONS = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        n = []
        for pos in POSITIONS:
            if self.colorAt(x + pos[0], y + pos[1]) == self.colorAt(x, y):
                n.append((x + pos[0], y + pos[1]))
        return n

    def dfs(self, x, y, visited):
        key = str(x) + ',' + str(y)
        if key in visited:
            return 0
        visited[key] = True
        result = 1
        for neighbor in self.neighbors(x, y):
            result += self.dfs(neighbor[0], neighbor[1], visited)
        return result

    def dfsIterative(self, x, y, visited):
        stack = [(x, y)]
        result = 0
        while len(stack) > 0:
            (x, y) = stack.pop()
            key = str(x) + ', ' + str(y)
            if key in visited:
                continue
            visited[key] = True

            result += 1
            for neighbor in self.neighbors(x, y):
                stack.append(neighbor)
        return result
#test input
grid = [[1, 0, 0, 1],
        [1, 1, 1, 0],
        [0, 1, 0, 0]]

print(Grid(grid).max_connected_colors())

#lesson 58
import heapq

def calcDistance(p):
    return p[0]*p[0] + p[1]*p[1]

def findClosestPoints(points, k):
    points = sorted(points, key = lambda x: calcDistance(x))
    return points[:k]

def findClosestPoints2(points, k):
    data = []
    for p in points:
        data.append((calcDistance(p), p))
    heapq.heapify(data)

    result = []
    for i in range(k):
        result.append(heapq.heappop(data)[1])
    return result

print (findClosestPoints2([[1, 1], [3, 3], [2, 2], [4, 4], [-1, -1]], 3))

print (findClosestPoints([[1, 1], [3, 3], [2, 2], [4, 4], [-1, -1]], 3))

#lesson 59
#autocompletion
class Node(object):
    def __init__(self, isWord, children):
        self.isWord = isWord
        #will be a dictionary, a:..., b:....
        self.children = children

class Solution:
    def build(self, words):
        trie = Node(False, {})
        for word in words:
            current = trie
            for char in word:
                if not char in current.children:
                    current.children[char] = Node(False, {})
                current = current.children[char]
            current.isWord = True
        self.trie = trie

    def autocomplete(self, word):
        current = self.trie
        for char in word:
            if not char in current.children:
                return []
            current = current.children[char]
        
        words = []
        #self.dfs(current, word, words)
        self.dfsIterative(current, word, words)
        return words
    
    def dfs(self, node, prefix, words):
        if node.isWord:
            words.append(prefix)
        for char in node.children:
            self.dfs(node.children[char], prefix + char, words)

    def dfsIterative(self, node, prefix, words):
        stack = [(node, prefix)]
        while len(stack):
            (node, prefix) = stack.pop()
            if node.isWord:
                words.append(prefix)
            for char in node.children:
                child = node.children[char]
                stack.append((child, prefix + char))

#test input
s = Solution()
s.build(['dog', 'dark', 'cat', 'door', 'dodge'])
print(s.autocomplete('do'))