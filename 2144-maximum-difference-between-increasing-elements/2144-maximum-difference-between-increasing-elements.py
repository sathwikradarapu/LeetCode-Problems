class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_ele=nums[0]
        max_diff=-1
        for i in range(1,len(nums)):
            min_ele=min(nums[i],min_ele)
            if nums[i]>min_ele:
                max_diff=max(max_diff,(nums[i]-min_ele))
        return max_diff
        