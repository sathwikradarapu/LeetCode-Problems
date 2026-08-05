class Solution:
    def sortColors(self, nums: List[int]) -> None:
        length=len(nums)
        left=0
        middle=0
        right=length-1
        while middle<=right:
            if nums[middle]==0:
                nums[middle]=nums[left]
                nums[left]=0
                left+=1
                middle+=1
            elif nums[middle]==1:
                middle+=1
            else:
                nums[middle]=nums[right]
                nums[right]=2
                right-=1