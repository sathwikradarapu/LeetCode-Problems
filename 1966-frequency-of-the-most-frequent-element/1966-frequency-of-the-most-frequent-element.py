class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxFreq,l,r,total,n=0,0,0,0,len(nums)

        for r in range(n):
            total+=nums[r]
            while(l+1<=r and (nums[r]*(r-l+1))>(total+k)):
                total-=nums[l]
                l+=1
            maxFreq=max(maxFreq,r-l+1)
        
        return maxFreq
