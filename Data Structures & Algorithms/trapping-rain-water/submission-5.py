class Solution:
    def trap(self, height: List[int]) -> int:
        max_left, max_right = [0]*len(height), [0]*len(height)
        maximumL, maximumR = 0, 0
        res, Sum = 0, 0
        for i in range(len(height)):
            if maximumL<height[i]:
                maximumL=height[i]
            max_left[i] = maximumL
        for i in range(len(height)-1,-1,-1):
            if maximumR<height[i]:
                maximumR=height[i]
            max_right[i] = maximumR
        for i in range(len(height)):
            Sum = min(max_left[i], max_right[i])-height[i]
            if Sum > 0:
                res+=Sum
        return res

        