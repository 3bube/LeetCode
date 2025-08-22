def canJump(nums):
    jumps = 0
    farthest = 0
    end = 0

    for i in range(len(nums) - 1):
        print(f"current index {i}\n")

        farthest = max(farthest, i + nums[i])

        print(f"farthest {farthest}\n")

        if i == end:
            print(f"Reached end {i} {end}\n")
            jumps += 1
            end = farthest
    return jumps


print(canJump([2,3,0,1,4]))