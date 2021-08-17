#Lesson 51
#Merge Intervals
def merge(intervals):
    results = []
    for start, end in sorted(intervals, key=lambda x:x[0]):
        #print(start)
        if results and start <= results[-1][1]:
            prev_start, prev_end = results[-1]
            results[-1] = (prev_start, max(prev_end, end))
        else:
            results.append((start, end))
    return results

#test input
print(merge(([1, 3], [5, 8], [4, 10], [20, 25])))

#Lesson 52
#Sell stock Max Profit
#brute force
def buy_and_sell(arr):
    max_profit = 0

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            max_profit = max(max_profit, arr[j] - arr[i])
    return max_profit

print(buy_and_sell([9, 11, 8, 5, 7, 10]))

def buy_and_sell2(arr):
    max_profit = 0
    max_current_price = 0
    for price in arr[::-1]:
        max_current_price = max(max_current_price, price)
        max_profit = max(max_profit, max_current_price - price)
    return max_profit

print(buy_and_sell2([9, 11, 8, 5, 7, 10]))

#Leson 53
#Phone Numbers
lettersMaps = {
    1: [],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
    0: []
}
validwords = ['dog', 'fish', 'cat', 'fog']

def makeWords_helper(digits, letters):
    if not digits:
        word = ''.join(letters)
        if word in validwords:
            return [word]
        return []

    results = []
    chars = lettersMaps[digits[0]]
    for char in chars:
        results += makeWords_helper(digits[1:], letters + [char])
    return results

def makeWords(phone):
    digits = []
    for digit in phone:
        digits.append(int(digit))
    return makeWords_helper(digits, [])

#test input
print(makeWords('364'))
