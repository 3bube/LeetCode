def threeSumClosest(self, nums, target):
    nums.sort()

    closest =  float("inf")


    for i in range(len(nums)):

        if i > 0 and nums[i] == nums[i - 1]:
            continue


        l,r = 0, len(nums) - 1

        while l < r:
            currentSum = nums[i] + nums[l] + nums[r]

            if abs(currentSum - target) < abs(closest - target):
                closest = currentSum


            if currentSum < target:
                l += 1
            elif currentSum > target:
                r -= 1
            else:
                return target
    
    return closest
            