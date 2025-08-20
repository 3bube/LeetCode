def zeroFilledSubarray(self, nums):
    count = 0
    total = 0
    for n in nums:
        if n == 0:
            count += 1
            total += count
        else:
            count = 0
    return total