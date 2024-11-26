class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(nums,k):
            l=0
            temp=0
            ans=float("-inf")
            n=len(nums)
            count=0
            dici={}
            for r in range(n):
                val=nums[r]
                if val not in dici:
                    dici[val]=1
                else:
                    dici[val]+=1
                while len(dici)>k:
                    lval=nums[l]
                    dici[lval]-=1
                    if dici[lval]==0:
                        dici.pop(lval)
                    l+=1
                ans=max(ans,r-l+1)
                count+=r-l+1
            return count
        a=atMostK(nums,k)
        b=atMostK(nums,k-1)
        c=a-b
        return c