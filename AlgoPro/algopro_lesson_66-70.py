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
            pal += c * (cnt//2)
        else:
            return False
    
    return pal + odd_char + pal[::-1]

#test input
print(find_palindrome('fofxo'))   