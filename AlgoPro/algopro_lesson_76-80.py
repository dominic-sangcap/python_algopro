#Lesson 76
#string to int
def convert_to_int(str):
  is_negative = False
  start_index = 0
  if str[0] == '-':
    is_negative = True
    start_index = 1

  result = 0
  for c in str[start_index:]:
    result = result * 10 + ord(c) - ord('0')

  if is_negative:
    result *= -1
  return result

#test input
print(convert_to_int('-105'))

#Lesson 77
#Shortest Unique Prefix
class Node:
  def __init__(self):
    self.count = 0
    self.children = {}
  
class Trie:
  def __init__(self):
    self.root = Node()

  def insert(self, word):
    node = self.root

    for c in word:
      if c not in node.children:
        node.children[c] = Node()
      node = node.children[c]
      node.count = node.count + 1
  
  def unique_prefix(self, word):
    node = self.root
    prefix = ''

    for c in word:
      if node.count == 1:
        return prefix
      else:
        node = node.children[c]
        prefix += c
    return prefix

def shortest_unique_prefix(words):
  trie = Trie()

  for word in words:
    trie.insert(word)
  
  unique_prefixes_list = []
  for word in words:
    unique_prefixes_list.append(trie.unique_prefix(word))


  return unique_prefixes_list

#test input
print(shortest_unique_prefix(['jon', 'john', 'jack', 'tech']))

#Lesson 78
#Make Largest NUmber
from functools import cmp_to_key

def largestNum(nums):
  sorted_nums = sorted(nums, 
  key=cmp_to_key(lambda a, b:
      1 if str(a) + str(b) < str(b) + str(a)
      else -1)
  )
  return ''.join(str(n) for n in sorted_nums)

#test input
print(largestNum([17, 7, 2, 45, 72]))

#Lesosn 79
#n queens
def nqueens_helper(n, row, col, asc_diag, desc_diag, queen_pos):
  if len(queen_pos) == n:
    return queen_pos

  curr_row = len(queen_pos)
  for curr_col in range(n):
    if col[curr_col] and row[curr_row] and asc_diag[curr_row + curr_col] and desc_diag[curr_row - curr_col]:
      col[curr_col] = False
      row[curr_row] = False
      asc_diag[curr_row + curr_col] = False
      desc_diag[curr_row - curr_col] = False

      queen_pos.append((curr_row, curr_col))
      nqueens_helper(n, row, col, asc_diag, desc_diag, queen_pos)

      if len(queen_pos) == n:
        return queen_pos

      # backtrack
      col[curr_col] = True
      row[curr_row] = True
      asc_diag[curr_row + curr_col] = True
      desc_diag[curr_row - curr_col] = True
      queen_pos.pop()

  return queen_pos


def nqueens(n):
  col = [True] * n
  row = [True] * n
  asc_diag = [True] * (n * 2 - 1)
  desc_diag = [True] * (n * 2 - 1)
  return nqueens_helper(n, col, row, asc_diag, desc_diag, [])

#test input
# Q . . . .
# . . . Q .
# . Q . . .
# . . . . Q
# . . Q . .
# [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)]
print(nqueens(5))
