class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        n=len(nums)
        temp=0
        ans=0
        for r in range(n):
            if nums[r]==0:
                temp+=1
            while temp>k:
                if nums[l]==0:
                    temp-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans