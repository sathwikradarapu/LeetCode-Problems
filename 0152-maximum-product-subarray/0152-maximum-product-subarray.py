class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        length=len(nums)
        prefix=[0]*length
        suffix=[0]*length
        prefix_number=1
        suffix_number=1
        max_product=float("-inf")
        for index in range(length):
            if prefix_number==0:
                prefix_number=1
            prefix_number=prefix_number*nums[index]
            prefix[index]=prefix_number
        for index in range(length-1,-1,-1):
            if suffix_number==0:
                suffix_number=1
            suffix_number=suffix_number*nums[index]
            suffix[index]=suffix_number
        max_product=max(max(prefix),max(suffix))
        return max_product