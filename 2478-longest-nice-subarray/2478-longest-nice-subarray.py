class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        

        l=0
        n=len(nums)
        bit_mask=0
        ans=float("-inf")
        for r in range(n):
            while(bit_mask&nums[r]!=0):
                bit_mask^=nums[l]
                l+=1
            bit_mask|=nums[r]
            ans=max(ans,r-l+1)
        return ans