class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums=sorted(nums)
        if len(nums)==1:
            return 0
        else:
            n=len(nums)
            l=0
            li=[]
            ans=float("inf")
            for r in range(n):
                li.append(nums[r])
                if r-l==k:
                    li.pop(0)
                    l+=1
                if r-l+1==k:
                    ans=min(ans,nums[r]-nums[l])
        return ans