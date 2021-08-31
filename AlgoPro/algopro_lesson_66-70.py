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
