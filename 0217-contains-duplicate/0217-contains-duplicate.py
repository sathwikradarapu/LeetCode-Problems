class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums1=set(nums)
        if len(nums1)==len(nums):
            return False
        return True