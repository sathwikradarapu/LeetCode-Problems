class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        c=0
        while min(nums)<k:
            c+=1
            nums.remove(min(nums))
        return c