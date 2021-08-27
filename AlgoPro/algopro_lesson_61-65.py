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