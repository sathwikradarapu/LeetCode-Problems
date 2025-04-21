class Solution:
    def findMin(self, nums: List[int]) -> int:
        #logn time means using binary search
        length=len(nums)
        left=0
        right=length-1
        while left<right:
            middle=(left+right)//2
            if nums[middle]>nums[right]:
                left=middle+1
            else:
                right=middle
        return nums[left]