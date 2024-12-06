class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_distinct = len(set(nums))
        n = len(nums)
        l = 0
        count = 0
        window_count = {}

        for r in range(n):
            # Add current element to the window
            if nums[r] not in window_count:
                window_count[nums[r]] = 0
            window_count[nums[r]] += 1

            # Shrink the window from the left while it has all distinct elements
            while len(window_count) == total_distinct:
                # Count subarrays from l to r and beyond
                count += n - r

                # Shrink the window
                window_count[nums[l]] -= 1
                if window_count[nums[l]] == 0:
                    del window_count[nums[l]]
                l += 1

        return count