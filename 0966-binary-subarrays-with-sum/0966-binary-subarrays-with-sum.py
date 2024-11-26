class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost1(nums,goal):
            if goal<0:
                return 0
            l=0
            temp=0
            ans=float("-inf")
            count=0
            n=len(nums)
            for r in range(n):
                if nums[r]==1:
                    temp+=1
                while temp>goal:
                    if nums[l]==1:
                        temp-=1
                    l+=1
                ans=max(ans,r-l+1)
                count+=r-l+1
            return count
        a=atMost1(nums,goal)
        b=atMost1(nums,goal-1)
        c=a-b
        return c