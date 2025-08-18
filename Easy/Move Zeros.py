def moveZeros(self, nums):
    k = 0
    n = len(nums) - 1

    for i in range(n):
        if nums[i] != 0:
            nums[k] = nums[i]
            k += 1
    
    for i in range(k, n):
        nums[i] = 0

    return nums