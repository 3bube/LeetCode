class Solution(object):
    def findErrorNums(self, nums):
        seen = {}

        for ch in nums:
            seen[ch] = seen.get(ch, 0) + 1

        duplicate = [k for k, v in seen.items() if v == 2][0]
        missing = [x for x in range(1, len(nums)+1) if x not in seen][0]

        return [duplicate, missing]
