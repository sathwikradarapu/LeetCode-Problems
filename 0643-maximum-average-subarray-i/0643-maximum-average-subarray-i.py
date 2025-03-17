class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=0
        n=len(nums)
        temp=0
        ans=float("-inf")
        for r in range(n):
            temp+=nums[r]
            if r-l==k:
                temp-=nums[l]
                l+=1
            if r-l+1==k:
                ans=max(ans,temp/k)
        return ans