#lesson 41
#Minimum Subarray Length
class Solution(object):
    def minSubArray(self, k, nums):
        leftIndex = rightIndex = 0
        sum = 0
        minLen = float('inf')

        while rightIndex < len(nums):
            sum += nums[rightIndex]
            while sum >= k:
                minLen = min(minLen, rightIndex - leftIndex + 1)
                sum -= nums[leftIndex]
                leftIndex += 1
            rightIndex += 1

        if minLen == float('inf'):
            return 0
        return minLen
#test input
print(Solution().minSubArray(7, [2, 3, 1, 2, 4, 3]))

#Lesson 42
#Merge List of Number Into Ranges
def makeRange(low, high):
    return str(low) + '-' + str(high)

def findRanges(nums):
    if not nums:
        return []

    ranges = []
    low = nums[0]
    high = nums[0]

    for n in nums:
        if high + 1 < n:
            ranges.append(makeRange(low, high))
            low = n
        high = n
    ranges.append(makeRange(low, high))
    return ranges

#test input
print(findRanges([0, 1, 2, 5, 7, 8, 9, 10, 11, 15]))