#Lesson 66
#Check for palindromes
from collections import defaultdict

def find_palindrome(str):
    char_counts = defaultdict(int)
    for c in str:
        char_counts[c] += 1

    pal = ''
    odd_char = ''
    for c, cnt in char_counts.items():
        if cnt % 2 == 0:
            pal += c * (cnt//2)
        elif odd_char == '':
            odd_char = c
            pal += c * (cnt//2) #unsure if this is actually needed
        else:
            return False
    
    return pal + odd_char + pal[::-1]

#test input
print(find_palindrome('fofxo'))   

#Lesson 67
class Rectangle(object):
    def __init__(self, min_x=0, min_y=0, max_x=0, max_y=0):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y

    def area(self):
        if self.min_x >= self.max_x:
            return 0
        if self.min_y >= self.max_y:
            return 0
        return (self.max_x - self.min_x) * (self.max_y - self.min_y) 

def intersect_rect(a, b):
    return Rectangle(
        max(a.min_x, b.min_x),
        max(a.min_y, b.min_y),
        min(a.max_x, b.max_x),
        min(a.max_y, b.max_y)
    )

#test input
a = Rectangle(0, 0, 3, 2)
b = Rectangle(1, 1, 3, 3)
intersesction = intersect_rect(a, b)
print(intersesction.area())

#Lesson 68
#Subtree
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left=left
        self.right=right

def pre(n):
    if not n:
        return 'null'
    return '-' + str(n.value) + '-' + pre(n.left) + '-' + pre(n.right)

def find_subtree(a, b):
    return pre(b) in pre(a)

#recursively find sollution
def find_subtree2(a, b):
  if not a:
    return False

  is_match = a.value == b.value
  if is_match:
    is_match_left = (not a.left or not b.left) or find_subtree2(a.left, b.left)
    if is_match_left:
      is_match_right = (not a.right or not b.right) or find_subtree2(
          a.right, b.right)
      if is_match_right:
        return True

  return find_subtree2(a.left, b) or find_subtree2(a.right, b)


#test input
n = Node(1)
n.left = Node(4)
n.right = Node(5)
n.left.left = Node(3)
n.left.right = Node(2)
n.right.left = Node(4)
n.right.right = Node(1)

b = Node(4)
b.left = Node(3)
b.right = Node(2)

print(find_subtree(n, b))

print(find_subtree2(n, b))

#Lesson 69
#Determine if Number

from enum import Enum

class DigitState(Enum):
    BEGIN = 0
    NEGATIVE1 = 1
    DIGIT1 = 2
    DOT = 3
    DIGIT2 = 4
    E = 5
    NEGATIVE2 = 6
    DIGIT3 =  7

STATE_VALIDATOR = {
    DigitState.BEGIN: lambda x: True,
    DigitState.DIGIT1: lambda x: x.isdigit(),
    DigitState.NEGATIVE1: lambda x: x == '-',
    DigitState.DIGIT2: lambda x: x.isdigit(),
    DigitState.DOT: lambda x: x == '.',
    DigitState.E: lambda x: x == 'e',
    DigitState.NEGATIVE2: lambda x: x == '-',
    DigitState.DIGIT3: lambda x: x.isdigit(),
}

NEXT_STATES_MAP = {
    DigitState.BEGIN: [DigitState.NEGATIVE1, DigitState.DIGIT1],
    DigitState.NEGATIVE1: [DigitState.DIGIT1, DigitState.DOT],
    DigitState.DIGIT1: [DigitState.DIGIT1, DigitState.DOT, DigitState.E],
    DigitState.DOT: [DigitState.DIGIT2],
    DigitState.DIGIT2: [DigitState.DIGIT2, DigitState.E],
    DigitState.NEGATIVE2: [DigitState.DIGIT3],
    DigitState.DIGIT3: [DigitState.DIGIT3],
}

def parse_number(str):
    state = DigitState.BEGIN

    for c in str:
        found = False
        for next_State in NEXT_STATES_MAP[state]:
            if STATE_VALIDATOR[next_State](c):
                state = next_State
                found = True
                break
        if not found:
            return False
    return state in [DigitState.DIGIT1, DigitState.DIGIT2, DigitState.DIGIT3]

#test input
print(parse_number('12.3'))

print(parse_number('12a'))

#Lesson 70
#First Recurring Character
def first_recurring_char(str):
    seen = set()

    for c in str:
        if c in seen:
            return c
        seen.add(c)

    return None
#test input
print(first_recurring_char('qwertty'))