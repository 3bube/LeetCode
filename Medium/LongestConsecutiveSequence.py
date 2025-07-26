# Medium
def longestConsecutive(nums):
    if not nums:
        return 0 

    res  = 0
    seen = set(nums)

    for num in nums:
        if num - 1 not in seen:
            streak = 1
            curr = num + 1
        
        while curr in seen:
            streak += 1
            curr += 1
        res = max(res, streak)

    return res

print(longestConsecutive([100,4,200,1,3,2])) # 4

        