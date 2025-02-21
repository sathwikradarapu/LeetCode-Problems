class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        res=1
        ans=1
        n=len(nums)
        if n==0:
            return 0
        for i in range(1,n):
            if nums[i]==nums[i-1]+1:
                res+=1
                ans=max(ans,res)
            else:
                res=1
        return ans
