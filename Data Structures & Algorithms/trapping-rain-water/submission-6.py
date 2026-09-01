class Solution:
    def trap(self, height: List[int]) -> int:
        #so calculate maximum from left and maximum from right
        left, right = [0]*len(height), [0]*len(height)
        lmax, rmax = 0, 0
        water = 0
        for i in range(len(height)):
            left[i] = lmax
            lmax = max(lmax, height[i])
        for i in range(len(height) - 1, -1, -1):
            right[i] = rmax
            rmax = max(rmax, height[i])
        for i in range(len(height)):
            if min(left[i],right[i]) < height[i]:
                continue
            else:
                water+=min(left[i], right[i]) - height[i]

        return water
                