class Solution:
    def trap(self, height: List[int]) -> int:
        length=len(height)
        left=0
        right=length-1
        totalWater=0
        leftMax=height[left]
        rightMax=height[right]
        while left<right:
            if leftMax<rightMax:
                left+=1
                leftMax=max(leftMax,height[left])
                totalWater+=leftMax-height[left]
            else:
                right-=1
                rightMax=max(rightMax,height[right])
                totalWater+=rightMax-height[right]
        return totalWater