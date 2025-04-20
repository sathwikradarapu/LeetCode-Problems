class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        prefix=[1]*length
        suffix=[1]*length
        result=[1]*length
        prefix_number=1
        suffix_number=1
        for index in range(1,length):
            prefix_number=prefix_number*nums[index-1]
            prefix[index]=prefix_number
        for index in range(length-2,-1,-1):
            suffix_number=suffix_number*nums[index+1]
            suffix[index]=suffix_number
        for index in range(length):
            result[index]=prefix[index]*suffix[index]
        return result
