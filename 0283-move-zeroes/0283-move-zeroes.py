class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left=0
        right=0
        length=len(nums)
        while right<length:
            if nums[right]!=0:
                temp=nums[left]
                nums[left]=nums[right]
                nums[right]=temp
                left+=1
            right+=1
        
                
