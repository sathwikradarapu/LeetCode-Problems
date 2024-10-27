class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans=0
        ans2=0
        for i in nums:
            if i==1:
                ans+=1
            else:
                ans=0
            ans2=max(ans2,ans)
        return ans2