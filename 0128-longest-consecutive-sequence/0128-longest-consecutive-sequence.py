class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums)==0:
            return 0
        nums=sorted(nums)
        length=len(nums)
        curr_length=1
        max_length=0
        for index in range(length-1):
            number1=nums[index]
            number2=nums[index+1]
            difference=number2-number1
            
            if difference==0:
                continue
            elif difference==1:
                curr_length+=1
                
            else:
                if curr_length>max_length:
                    max_length=curr_length
                    
                curr_length=1
        max_length=max(max_length,curr_length)
        return(max_length)