def applyOperation(self, nums):
    n = len(nums) - 1

    for i in range(n):
        if nums[i] == nums[i + 1]:
            nums[i] *= 2
            nums[i + 1] = 0
    return [x for x in nums if x != 0] + [x for x in nums if x == 0]