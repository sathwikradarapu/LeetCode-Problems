class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        #bruteforce
        length=len(nums)
        for index in range(length):
            current_number=nums[index]
            if index==0:
                if length!=1:
                    next_number=nums[index+1]
                    if current_number>next_number:
                        return index
                else:
                    return index
            elif index==length-1:
                previous_number=nums[index-1]
                if current_number>previous_number:
                    return index
            else:
                previous_number=nums[index-1]
                next_number=nums[index+1]
                if current_number>previous_number and current_number>next_number:
                    return index
        return 0
