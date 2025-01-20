class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:
            return  # Handle empty list case
        k %= n  # To handle cases where k > n
        nums[:] = nums[-k:] + nums[:-k]  # Rotate the list in one step