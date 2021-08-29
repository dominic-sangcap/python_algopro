#Lesson 61
#Roman Numerals to Decimal
class Solution:
    def romanToInt(self, s):
        romanNumerals = {
            'I': 1, 
            'V': 5, 
            'X': 10,
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000
        }

        prev = 0
        sum = 0
        for i in s[::-1]:
            curr = romanNumerals[i]
            if prev > curr:
                sum -= curr
            else:
                sum += curr
            prev = curr
        return sum

#test input
n = 'MCMIV'
print(Solution().romanToInt(n))

#Lesson 62
#Subarray With Target Sum
#brute force
def find_continuous_k(list, k):
    for start in range(len(list)):
        sum = 0
        for end in range(start, len(list)):
            sum += list[end]
            if sum == k:
                return list[start:end + 1]
    return None

#test input
print(find_continuous_k([1, 3, 2, 5, 7, 2], 14))

#sum mapping approach
def find_continuous_k(list, k):
    previous_sums = {0 : -1}
    sum = 0
    for index, n in enumerate(list):
        sum += n
        previous_sums[sum] = index
        if previous_sums.get(sum - k):
            return list[previous_sums[sum-k] + 1: index + 1]
    return None

#test input
print(find_continuous_k([1, 3, 2, 5, 7, 2], 14))

#Lesson 63
##Absolute Paths
def clean_path(path):
    folders = path.split('/')
    stack = []

    for folder in folders:
        if folder == '.':
            pass
        elif folder == '..':
            stack.pop()
        else:
            stack.append(folder)
    return'/'.join(stack)

#test input
path = '/users/tech/docs/.././desk/../'
print(clean_path(path))

#Lesson 64
#Consecutive Bit Ones
def longest_run(n):
    longest_run = 0
    current_run = 0
    BITMASK = 1

    while n != 0:
        if n & BITMASK == 0:
            longest_run = max(longest_run, current_run)
            current_run = 0
        else:
            current_run += 1
        n = n >> 1
    longest_run = max(longest_run, current_run)
    return longest_run

#test input
n = 242
print(longest_run(n))

#Lesson 65
#Anagrams in a String
from collections import defaultdict

def find_anagrams(a, b):
    char_map = defaultdict(int)

    for c in b:
        char_map[c] += 1

    results = []
    for i in range(len(a)):
        c = a[i]

        if i >= len(b):
            c_old = a[i-len(b)]
            char_map[c_old] += 1
            if char_map[c_old] == 0:
                del char_map[c_old]

        char_map[c] -= 1
        if char_map[c] == 0:
            del char_map[c]

        if i + 1 >= len(b) and len(char_map) == 0:
            results.append(i - len(b) + 1)

    return results

#test input
print(find_anagrams('acdbacdacb', 'abc'))
