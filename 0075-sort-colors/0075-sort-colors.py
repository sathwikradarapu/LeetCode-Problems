class Solution:
    def sortColors(self, nums: List[int]) -> None:
        length=len(nums)
        left=0
        mid=0
        right=length-1
        while mid<=right:
            if nums[mid]==1:
                mid+=1
            elif nums[mid]==0:
                nums[mid]=nums[left]
                nums[left]=0
                left+=1
                mid+=1
            else:
                nums[mid]=nums[right]
                nums[right]=2
                right-=1
        
        
