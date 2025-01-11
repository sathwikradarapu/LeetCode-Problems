class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums=sorted(nums)
        a=nums[0]
        b=nums[1]
        c=nums[-1]
        d=nums[-2]
        e=(c*d)-(a*b)
        return e
