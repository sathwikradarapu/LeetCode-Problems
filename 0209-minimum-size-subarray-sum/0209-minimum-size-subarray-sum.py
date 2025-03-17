class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        n=len(nums)
        temp=0
        ans=float("inf")
        for r in range(n):
            temp+=nums[r]
            while temp>=target:
                ans=min(ans,r-l+1)
                temp-=nums[l]
                l+=1
        if target>sum(nums):
            return 0
        return ans