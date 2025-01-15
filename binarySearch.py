# Easy
def binarySearch(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + (r - l) // 2

        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1

print(binarySearch([1,2,3,4,5,6,7,8,9,10], 5)) # 4