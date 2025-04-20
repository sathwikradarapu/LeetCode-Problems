class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix=1
        suffix=1
        length=len(nums)
        max_product=float("-inf")
        for index in range(length):
            #if 0 occurs then considering new sub array
            if(prefix==0):
                prefix=1
            #if 0 occurs then considering new sub array
            if(suffix==0):
                suffix=1
            prefix*=nums[index]
            suffix*=nums[length-index-1]
            max_product=max(max_product,max(prefix,suffix))
        return max_product