class Solution(object):
    def findMaxAverage(self, nums, k):
        windowSum = sum(nums[:k])
        maxSum = windowSum


        for i in range(k, len(nums)):
            windowSum += nums[i] - nums[i - k]
            maxSum = max(windowSum, maxSum)
        return float(maxSum) / k