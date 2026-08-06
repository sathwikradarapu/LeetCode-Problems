class Solution:
    def maxArea(self, height: List[int]) -> int:
        length=len(height)
        left=0
        right=length-1
        max_area=float("-inf")
        while left<right:
            hei=min(height[left],height[right])
            wid=right-left
            area=hei*wid
            max_area=max(area,max_area)
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
        return max_area
