class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_distinct = len(set(nums))
        n = len(nums)
        l = 0
        count = 0
        window_count = {}

        for r in range(n):
            if nums[r] not in window_count:
                window_count[nums[r]] = 1
            else:
                window_count[nums[r]] += 1
            while len(window_count) == total_distinct:
                window_count[nums[l]] -= 1
                if window_count[nums[l]] == 0:
                    del window_count[nums[l]]
                l += 1
                count += n-r
        return count