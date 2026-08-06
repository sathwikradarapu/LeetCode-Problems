class Solution:
    def maxArea(self, height: List[int]) -> int:
        length=len(height)
        left=0
        right=length-1
        max_area=float("-inf")
        while left<right:
            height_left=height[left]
            height_right=height[right]
            min_height=min(height_left,height_right)
            width=right-left
            area=min_height*width
            max_area=max(max_area,area)
            if height_left<=height_right:
                left+=1
            else:
                right-=1
        return max_area