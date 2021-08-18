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

#Lesson 54
#QuickSelect
import heapq

#brute force
def findKthLargest(arr, k):
    for i in range(0, k):
        (max_value, max_index) = (arr[0], 0)
        for j in range(0, len(arr)):
            if max_value < arr[j]:
                (max_value, max_index) = arr[j], j
        arr = arr[:max_index] + arr[max_index + 1:]
    for j in range(0, len(arr)):
            if max_value < arr[j]:
                (max_value, max_index) = arr[j], j
    return max_value

#nlogn time
def findKthLargest2(arr, k):
    return sorted(arr)[-k]

#heap implementation
def findKthLargest3(arr, k):
    arr = list(map(lambda x: -x, arr))
    heapq.heapify(arr)
    for i in range(0, k - 1):
        heapq.heappop(arr)
    return -arr[0]

#quicslect implmentation
def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quickselect(arr, k):
    k = len(arr) - k
    left = 0
    right = len(arr) - 1

    while left <= right:
        pivotIndex = partition(arr, left, right)
        if pivotIndex == k:
            return arr[pivotIndex]
        elif pivotIndex > k:
            right = pivotIndex - 1
        else:
            left = pivotIndex + 1
    return -1

#test input
print(quickselect([8, 7, 2, 3, 4, 1, 5, 6, 9, 0], 4))

print(findKthLargest3([8, 7, 2, 3, 4, 1, 5, 6, 9, 0], 4))

print(findKthLargest2([8, 7, 2, 3, 4, 1, 5, 6, 9, 0], 4))

print(findKthLargest([8, 7, 2, 3, 4, 1, 5, 6, 9, 0], 4))