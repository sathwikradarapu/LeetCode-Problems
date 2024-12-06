class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_distinct = len(set(nums))
    
        n = len(nums)
        count = 0

        # Iterate through all possible subarrays
        for start in range(n):
            # Use a set to track unique elements in the current subarray
            unique_elements = set()
            for end in range(start, n):
                unique_elements.add(nums[end])
                # If the subarray has all distinct elements, it's complete
                if len(unique_elements) == total_distinct:
                    count += 1
        
        return count