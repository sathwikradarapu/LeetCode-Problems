class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        max_left=[0]*n
        l_max=0
        for i in range(n):
            max_left[i]=l_max
            l_max=max(l_max,height[i])
        max_right=[0]*n
        r_max=0
        for i in range(n-1,-1,-1):
            max_right[i]=r_max
            r_max=max(r_max,height[i])
        ans=0
        for i in range(n):
            diff=min(max_left[i],max_right[i])
            diff=diff-height[i]
            if diff>0:
                ans+=diff
        return ans
            