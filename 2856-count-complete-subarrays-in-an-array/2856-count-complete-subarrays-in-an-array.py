class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        c=0
        a=len(set(nums))
        for i in range(len(nums)):
            sub=set()
            for j in range(i,len(nums)):
                sub.add(nums[j])
                if a==len(sub):
                    c+=1
        return c