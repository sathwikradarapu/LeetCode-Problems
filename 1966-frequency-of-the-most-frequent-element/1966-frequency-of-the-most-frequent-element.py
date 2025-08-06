class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,total,maxCount=0,0,0
        for r in range(len(nums)):
            total+=nums[r]
            while(((nums[r]*(r-l+1))>(total+k)) and l+1<=r):
                total-=nums[l]
                l+=1
            maxCount=max(maxCount,r-l+1)
        return maxCount
