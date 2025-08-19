def maxArea(self, height):
    l, r = 0, len(height) - 1

    maxArea = 0

    while l < r:
        currArea = min(height[l], height[r]) * (r - l)
        maxArea = (currArea, maxArea)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return maxArea