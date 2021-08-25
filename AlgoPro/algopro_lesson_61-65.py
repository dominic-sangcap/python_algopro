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