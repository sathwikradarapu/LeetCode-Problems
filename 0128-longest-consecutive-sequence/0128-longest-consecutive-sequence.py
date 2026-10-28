class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        #bruteforce
        if len(nums)==0:
            return 0
        else:
            length=len(nums)
            nums=sorted(nums)
            current_length=1
            maximum_length=float("-inf")
            for index in range(length-1):
                number1=nums[index]
                number2=nums[index+1]
                difference=number2-number1
                if difference==0:
                    continue
                elif difference==1:
                    current_length+=1
                else:
                    maximum_length=max(maximum_length,current_length)
                    current_length=1
            maximum_length=max(maximum_length,current_length)
            return maximum_length