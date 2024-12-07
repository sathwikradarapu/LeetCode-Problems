class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n=len(nums)
        ans2=float("inf")
        for i in range(n):
            for j in range(i+1,n+1):
                sub=nums[i:j]
                if len(sub)>=l and len(sub)<=r:
                    ans=sum(sub)
                    if ans>0:
                        ans2=min(ans2,ans)
        if ans2<float("inf"):
            return ans2
        else:
            return -1

        