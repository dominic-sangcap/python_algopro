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
