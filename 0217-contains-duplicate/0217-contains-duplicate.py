class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ans=False
        nums=sorted(nums)
        for i in range(len(nums)):
            if i!=len(nums)-1:
                if nums[i]==nums[i+1]:
                    ans=True
                    break
        return ans