class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            a=min(nums)
            b=nums.index(a)
            a=a*multiplier
            nums[b]=a
        return nums