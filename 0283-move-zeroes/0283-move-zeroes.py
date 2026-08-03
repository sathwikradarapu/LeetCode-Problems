class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left=0
        right=0
        length=len(nums)
        while right<length:
            if nums[right]!=0:
                temp=nums[right]
                nums[right]=nums[left]
                nums[left]=temp
                left+=1
            right+=1
        
                
