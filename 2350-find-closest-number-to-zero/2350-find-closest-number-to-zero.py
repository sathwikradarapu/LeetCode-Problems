class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans=nums[0]
        for i in nums:
            if abs(i)<abs(ans):
                ans=i
        if ans<0 and abs(ans) in nums:
            return abs(ans)
        return ans