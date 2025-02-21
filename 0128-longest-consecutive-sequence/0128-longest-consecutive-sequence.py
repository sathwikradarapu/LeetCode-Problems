class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 1  # Tracks the current sequence length
        ans = 1  # Tracks the max sequence length
        if n==0:
            return 0
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:  # If consecutive, increase length
                res += 1
                ans = max(ans, res)
            elif nums[i] != nums[i - 1]:  # Ignore duplicate values, but reset count
                res = 1  

        return ans
