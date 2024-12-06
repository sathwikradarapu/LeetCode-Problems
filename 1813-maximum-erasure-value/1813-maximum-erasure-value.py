class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l=0
        n=len(nums)
        ans=0
        uniset=set()
        for r in range(n):
            ch=nums[r]
            if ch not in uniset:
                uniset.add(ch)
            else:
                while ch in uniset:
                    uniset.remove(nums[l])
                    l+=1
                uniset.add(ch)
            ans=max(ans,sum(uniset))
        return ans