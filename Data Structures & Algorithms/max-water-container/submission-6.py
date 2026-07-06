class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVolume = 0
        l, r = 0, len(heights) - 1
        while l < r:
            newVolume = (r - l)*min(heights[l], heights[r])
            maxVolume = max(maxVolume, newVolume)

            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        return maxVolume
