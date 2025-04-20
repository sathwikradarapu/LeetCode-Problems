class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length=len(nums)
        prefix=[0]*length
        suffix=[0]*length
        prefix_number=0
        suffix_number=0
        max_sum=0
        for index in range(length):
            if prefix_number<0:
                prefix_number=0
            prefix_number=prefix_number+nums[index]
            prefix[index]=prefix_number
        for index in range(length-1,-1,-1):
            if suffix_number<0:
                suffix_number=0
            suffix_number=suffix_number+nums[index]
            suffix[index]=suffix_number
        max_sum=max(max(prefix),max(suffix))
        return max_sum
