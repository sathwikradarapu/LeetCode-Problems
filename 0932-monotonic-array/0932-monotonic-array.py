class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[-1]-nums[0]<0:
            nums.reverse()
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                return False
        return True