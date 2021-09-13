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